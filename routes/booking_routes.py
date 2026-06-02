from io import BytesIO

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import abort
from flask import send_file

from reportlab.pdfgen import canvas

from flask_login import (
    login_required,
    current_user
)

from services.booking_service import (
    BookingService
)

from services.qr_service import (
    QRService
)

booking_bp = Blueprint(
    "booking",
    __name__,
    url_prefix="/bookings"
)

booking_service = BookingService()

qr_service = QRService()


@booking_bp.route("/")
@login_required
def bookings():

    bookings = (
        booking_service
        .get_user_bookings(
            current_user.id
        )
    )

    return render_template(
        "bookings/index.html",
        bookings=bookings
    )


@booking_bp.route(
    "/create/<int:flight_id>"
)
@login_required
def create_booking(
    flight_id
):

    booking = (
        booking_service
        .create_flight_booking(
            current_user.id,
            flight_id
        )
    )

    if not booking:
        abort(404)

    return redirect(
        f"/bookings/details/{booking.booking_reference}"
    )


@booking_bp.route(
    "/details/<booking_reference>"
)
@login_required
def booking_details(
    booking_reference
):

    booking = (
        booking_service
        .get_booking_by_id(
            booking_reference
        )
    )

    if not booking:
        abort(404)

    return render_template(
        "bookings/details.html",
        booking=booking
    )


@booking_bp.route(
    "/ticket/<booking_reference>"
)
@login_required
def download_ticket(
    booking_reference
):

    booking = (
        booking_service
        .get_booking_by_id(
            booking_reference
        )
    )

    if not booking:
        abort(404)

    pdf_buffer = BytesIO()

    pdf = canvas.Canvas(
        pdf_buffer
    )

    pdf.setTitle(
        "FlightHub Ticket"
    )

    pdf.drawString(
        100,
        800,
        "FlightHub Ticket"
    )

    pdf.drawString(
        100,
        770,
        f"Reference: {booking.booking_reference}"
    )

    pdf.drawString(
        100,
        740,
        f"Passenger: {current_user.username}"
    )

    pdf.drawString(
        100,
        710,
        f"Status: {booking.booking_status}"
    )

    pdf.drawString(
        100,
        680,
        f"Seat: {booking.seat_number}"
    )

    pdf.drawString(
        100,
        650,
        f"Class: {booking.travel_class}"
    )

    pdf.drawString(
        100,
        620,
        f"Price: {booking.total_price} SEK"
    )

    if booking.flight:

        pdf.drawString(
            100,
            590,
            f"Flight: {booking.flight.flight_number}"
        )

    pdf.save()

    pdf_buffer.seek(0)

    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name=(
            f"{booking.booking_reference}.pdf"
        ),
        mimetype="application/pdf"
    )


@booking_bp.route(
    "/qr/<booking_reference>"
)
@login_required
def booking_qr(
    booking_reference
):

    booking = (
        booking_service
        .get_booking_by_id(
            booking_reference
        )
    )

    if not booking:
        abort(404)

    return render_template(
        "bookings/qr.html",
        booking=booking
    )


@booking_bp.route(
    "/qr-image/<booking_reference>"
)
@login_required
def booking_qr_image(
    booking_reference
):

    booking = (
        booking_service
        .get_booking_by_id(
            booking_reference
        )
    )

    if not booking:
        abort(404)

    qr_image = (
        qr_service
        .generate_booking_qr(
            booking
        )
    )

    return send_file(
        qr_image,
        mimetype="image/png"
    )


@booking_bp.route(
    "/cancel/<booking_reference>"
)
@login_required
def cancel_booking(
    booking_reference
):

    booking_service.cancel_booking(
        booking_reference
    )

    return redirect(
        f"/bookings/details/{booking_reference}"
    )
