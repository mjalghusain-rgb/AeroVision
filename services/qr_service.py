import qrcode

from io import BytesIO


class QRService:

    def generate_booking_qr(
        self,
        booking
    ):

        qr_data = f"""
BOOKING={booking.booking_reference}
STATUS={booking.booking_status}
FLIGHT={booking.flight.flight_number if booking.flight else 'N/A'}
USER={booking.user.username if booking.user else 'N/A'}
"""

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )

        qr.add_data(
            qr_data
        )

        qr.make(
            fit=True
        )

        image = qr.make_image()

        buffer = BytesIO()

        image.save(
            buffer,
            format="PNG"
        )

        buffer.seek(0)

        return buffer
