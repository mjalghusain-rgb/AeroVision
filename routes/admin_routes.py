from flask import Blueprint
from flask import render_template
from flask import abort
from flask import redirect
from flask import url_for

from flask_login import (
    login_required,
    current_user
)

from database.models import (
    User,
    Flight,
    Hotel,
    Car,
    Notification,
    FlightBooking
)

from services.aviationstack_sync_service import (
    AviationStackSyncService
)

from services.airport_enrichment_service import (
    AirportEnrichmentService
)

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

sync_service = (
    AviationStackSyncService()
)

airport_enrichment_service = (
    AirportEnrichmentService()
)


@admin_bp.route("/")
@login_required
def admin():

    if current_user.role != "admin":
        abort(403)

    stats = {

        "users":
            User.query.count(),

        "flights":
            Flight.query.count(),

        "hotels":
            Hotel.query.count(),

        "cars":
            Car.query.count(),

        "notifications":
            Notification.query.count(),

        "bookings":
            FlightBooking.query.count(),

        "confirmed_bookings":
            FlightBooking.query.filter_by(
                booking_status="Confirmed"
            ).count(),

        "cancelled_bookings":
            FlightBooking.query.filter_by(
                booking_status="Cancelled"
            ).count(),

        "revenue":
            sum(
                booking.total_price
                for booking in
                FlightBooking.query.all()
            )

    }

    return render_template(
        "admin/index.html",
        stats=stats
    )


@admin_bp.route("/sync-flights")
@login_required
def sync_flights():

    if current_user.role != "admin":
        abort(403)

    sync_service.sync_flights(
        100
    )

    return redirect(
        url_for(
            "admin.admin"
        )
    )


@admin_bp.route("/enrich-airports")
@login_required
def enrich_airports():

    if current_user.role != "admin":
        abort(403)

    airport_enrichment_service.enrich_airports()

    return redirect(
        url_for(
            "admin.admin"
        )
    )


@admin_bp.route("/users")
@login_required
def users():

    if current_user.role != "admin":
        abort(403)

    users = (
        User.query
        .order_by(User.id.desc())
        .all()
    )

    return render_template(
        "admin/users.html",
        users=users
    )


@admin_bp.route("/users/<int:user_id>")
@login_required
def user_details(user_id):

    if current_user.role != "admin":
        abort(403)

    user = User.query.get_or_404(
        user_id
    )

    return render_template(
        "admin/user_details.html",
        user=user
    )


@admin_bp.route("/bookings")
@login_required
def bookings():

    if current_user.role != "admin":
        abort(403)

    bookings = (
        FlightBooking.query
        .order_by(
            FlightBooking.id.desc()
        )
        .all()
    )

    return render_template(
        "admin/bookings.html",
        bookings=bookings
    )
