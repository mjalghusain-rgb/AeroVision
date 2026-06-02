import requests

from config import Config


class AviationStackService:

    def __init__(self):

        self.api_key = (
            Config.AVIATIONSTACK_API_KEY
        )

        self.base_url = (
            Config.AVIATIONSTACK_API_URL
        )

    def get_flights(
        self,
        limit=20
    ):

        url = (
            f"{self.base_url}/flights"
        )

        params = {

            "access_key":
                self.api_key,

            "limit":
                limit

        }

        response = requests.get(
            url,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def search_flights(
        self,
        query
    ):

        data = self.get_flights(
            100
        )

        flights = (
            data.get(
                "data",
                []
            )
        )

        query = (
            query.lower()
        )

        results = []

        for flight in flights:

            airline = (
                flight.get(
                    "airline",
                    {}
                ).get(
                    "name",
                    ""
                )
            )

            flight_iata = (
                flight.get(
                    "flight",
                    {}
                ).get(
                    "iata",
                    ""
                )
            )

            departure = (
                flight.get(
                    "departure",
                    {}
                ).get(
                    "iata",
                    ""
                )
            )

            arrival = (
                flight.get(
                    "arrival",
                    {}
                ).get(
                    "iata",
                    ""
                )
            )

            if (

                query in airline.lower()

                or

                query in flight_iata.lower()

                or

                query in departure.lower()

                or

                query in arrival.lower()

            ):

                results.append(
                    flight
                )

        return results
