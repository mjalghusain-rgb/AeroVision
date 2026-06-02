from data.airport_services import AIRPORT_SERVICES


class AirportServicesService:

    def __init__(self):

        self.services = AIRPORT_SERVICES

    def get_all_airports(self):

        return list(
            self.services.keys()
        )

    def get_services(
        self,
        airport_code
    ):

        airport_code = (
            airport_code.upper()
        )

        return self.services.get(
            airport_code
        )

    def airport_exists(
        self,
        airport_code
    ):

        airport_code = (
            airport_code.upper()
        )

        return (
            airport_code
            in
            self.services
        )

    def get_restaurants(
        self,
        airport_code
    ):

        airport = self.get_services(
            airport_code
        )

        if not airport:
            return []

        return airport.get(
            "restaurants",
            []
        )

    def get_lounges(
        self,
        airport_code
    ):

        airport = self.get_services(
            airport_code
        )

        if not airport:
            return []

        return airport.get(
            "lounges",
            []
        )

    def get_parking(
        self,
        airport_code
    ):

        airport = self.get_services(
            airport_code
        )

        if not airport:
            return []

        return airport.get(
            "parking",
            []
        )

    def get_transport(
        self,
        airport_code
    ):

        airport = self.get_services(
            airport_code
        )

        if not airport:
            return []

        return airport.get(
            "transport",
            []
        )
