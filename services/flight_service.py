from database.models import (
    Flight
)


class FlightService:

    def get_all_flights(self):

        return (
            Flight.query
            .order_by(
                Flight.id.desc()
            )
            .all()
        )

    def get_flight_by_number(
        self,
        flight_number
    ):

        return (
            Flight.query
            .filter_by(
                flight_number=flight_number
            )
            .first()
        )

    def search(
        self,
        query
    ):

        return (
            Flight.query
            .filter(
                Flight.flight_number.contains(
                    query
                )
            )
            .all()
        )

    def get_arrivals(
        self,
        airport_id
    ):

        return (
            Flight.query
            .filter_by(
                arrival_airport_id=airport_id
            )
            .all()
        )

    def get_departures(
        self,
        airport_id
    ):

        return (
            Flight.query
            .filter_by(
                departure_airport_id=airport_id
            )
            .all()
        )

    def total_flights(self):

        return (
            Flight.query.count()
        )
