from datetime import datetime

from database.models import (
    db,
    Airline,
    Airport,
    Flight
)

from services.aviationstack_service import (
    AviationStackService
)


class AviationStackSyncService:

    def __init__(self):

        self.api = (
            AviationStackService()
        )

    def sync_flights(
        self,
        limit=20
    ):

        data = (
            self.api.get_flights(
                limit
            )
        )

        flights = (
            data.get(
                "data",
                []
            )
        )

        imported = 0

        for item in flights:

            airline_name = (
                item.get(
                    "airline",
                    {}
                ).get(
                    "name"
                )
            )

            airline_iata = (
                item.get(
                    "airline",
                    {}
                ).get(
                    "iata"
                )
            )

            departure = (
                item.get(
                    "departure",
                    {}
                )
            )

            arrival = (
                item.get(
                    "arrival",
                    {}
                )
            )

            flight_data = (
                item.get(
                    "flight",
                    {}
                )
            )

            aircraft = (
                item.get(
                    "aircraft"
                ) or {}
            )

            if not airline_name:
                continue

            airline = (
                Airline.query.filter_by(
                    name=airline_name
                ).first()
            )

            if not airline:

                airline = Airline(
                    name=airline_name,
                    iata_code=airline_iata,
                    country="Unknown",
                    website=""
                )

                db.session.add(
                    airline
                )

                db.session.flush()

            dep_airport = (
                Airport.query.filter_by(
                    iata_code=departure.get(
                        "iata"
                    )
                ).first()
            )

            if not dep_airport:

                dep_airport = Airport(
                    name=departure.get(
                        "airport"
                    ),
                    city="Unknown",
                    country="Unknown",
                    iata_code=departure.get(
                        "iata"
                    ),
                    icao_code=departure.get(
                        "icao"
                    ),
                    terminals=1
                )

                db.session.add(
                    dep_airport
                )

                db.session.flush()

            arr_airport = (
                Airport.query.filter_by(
                    iata_code=arrival.get(
                        "iata"
                    )
                ).first()
            )

            if not arr_airport:

                arr_airport = Airport(
                    name=arrival.get(
                        "airport"
                    ),
                    city="Unknown",
                    country="Unknown",
                    iata_code=arrival.get(
                        "iata"
                    ),
                    icao_code=arrival.get(
                        "icao"
                    ),
                    terminals=1
                )

                db.session.add(
                    arr_airport
                )

                db.session.flush()

            flight_number = (
                flight_data.get(
                    "iata"
                )
            )

            if not flight_number:
                continue

            exists = (
                Flight.query.filter_by(
                    flight_number=flight_number
                ).first()
            )

            if exists:
                continue

            departure_time = None
            arrival_time = None

            try:

                if departure.get(
                    "scheduled"
                ):

                    departure_time = (
                        datetime.fromisoformat(
                            departure.get(
                                "scheduled"
                            ).replace(
                                "Z",
                                "+00:00"
                            )
                        )
                    )

            except Exception:
                pass

            try:

                if arrival.get(
                    "scheduled"
                ):

                    arrival_time = (
                        datetime.fromisoformat(
                            arrival.get(
                                "scheduled"
                            ).replace(
                                "Z",
                                "+00:00"
                            )
                        )
                    )

            except Exception:
                pass

            flight = Flight(

                flight_number=flight_number,

                airline_id=airline.id,

                departure_airport_id=(
                    dep_airport.id
                ),

                arrival_airport_id=(
                    arr_airport.id
                ),

                departure_time=(
                    departure_time
                ),

                arrival_time=(
                    arrival_time
                ),

                terminal=(
                    departure.get(
                        "terminal"
                    ) or ""
                ),

                gate=(
                    departure.get(
                        "gate"
                    ) or ""
                ),

                aircraft_type=(
                    aircraft.get(
                        "icao"
                    ) or
                    aircraft.get(
                        "iata"
                    ) or
                    ""
                ),

                status=item.get(
                    "flight_status",
                    "scheduled"
                )

            )

            db.session.add(
                flight
            )

            imported += 1

        db.session.commit()

        return imported
