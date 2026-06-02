from datetime import datetime
import uuid

from database.models import (
    db,
    FlightBooking,
    Flight
)


class BookingService:

    def get_all_bookings(self):

        return (
            FlightBooking.query
            .order_by(
                FlightBooking.id.desc()
            )
            .all()
        )

    def get_booking_by_id(
        self,
        booking_id
    ):

        return (
            FlightBooking.query
            .filter_by(
                booking_reference=booking_id
            )
            .first()
        )

    def get_booking_by_db_id(
        self,
        booking_id
    ):

        return (
            FlightBooking.query
            .get(
                booking_id
            )
        )

    def get_user_bookings(
        self,
        user_id
    ):

        return (
            FlightBooking.query
            .filter_by(
                user_id=user_id
            )
            .order_by(
                FlightBooking.id.desc()
            )
            .all()
        )

    def create_flight_booking(
        self,
        user_id,
        flight_id
    ):

        flight = (
            Flight.query.get(
                flight_id
            )
        )

        if not flight:
            return None

        booking_reference = (
            str(
                uuid.uuid4()
            )[:8]
            .upper()
        )

        booking = FlightBooking(

            booking_reference=
            booking_reference,

            user_id=user_id,

            flight_id=flight_id,

            booking_status=
            "Confirmed",

            seat_number=
            "AUTO",

            travel_class=
            "Economy",

            total_price=
            99.99,

            created_at=
            datetime.utcnow()

        )

        db.session.add(
            booking
        )

        db.session.commit()

        return booking

    def cancel_booking(
        self,
        booking_reference
    ):

        booking = (
            self.get_booking_by_id(
                booking_reference
            )
        )

        if not booking:
            return False

        booking.booking_status = (
            "Cancelled"
        )

        db.session.commit()

        return True

    def total_bookings(self):

        return (
            FlightBooking.query
            .count()
        )

    def total_confirmed(self):

        return (
            FlightBooking.query
            .filter_by(
                booking_status=
                "Confirmed"
            )
            .count()
        )
