from flask import Blueprint
from flask import render_template

from flask_login import (
    login_required,
    current_user
)

from database.models import (
    User,
    Flight,
    Hotel,
    Car,
    Notification
)

dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard"
)


@dashboard_bp.route("/")
@login_required
def dashboard():

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
            Notification.query.count()

    }

    return render_template(
        "dashboard/dashboard.html",
        user=current_user,
        stats=stats
    )
