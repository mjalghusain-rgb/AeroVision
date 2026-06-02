from data.hotels import HOTELS


class HotelService:

    def __init__(self):

        self.hotels = HOTELS

    def get_all_hotels(self):

        return self.hotels

    def get_hotel_by_id(
        self,
        hotel_id
    ):

        hotel_id = hotel_id.upper()

        for hotel in self.hotels:

            if (
                hotel["hotel_id"]
                == hotel_id
            ):

                return hotel

        return None

    def search(
        self,
        query
    ):

        query = query.lower()

        results = []

        for hotel in self.hotels:

            if (

                query in hotel["hotel_id"].lower()

                or

                query in hotel["name"].lower()

                or

                query in hotel["city"].lower()

                or

                query in hotel["country"].lower()

                or

                query in hotel["status"].lower()

            ):

                results.append(
                    hotel
                )

        return results

    def get_by_city(
        self,
        city
    ):

        city = city.lower()

        results = []

        for hotel in self.hotels:

            if (
                hotel["city"].lower()
                == city
            ):

                results.append(
                    hotel
                )

        return results

    def get_by_status(
        self,
        status
    ):

        status = status.lower()

        results = []

        for hotel in self.hotels:

            if (
                hotel["status"].lower()
                == status
            ):

                results.append(
                    hotel
                )

        return results

    def total_hotels(self):

        return len(
            self.hotels
        )

    def available_hotels(self):

        return len(
            self.get_by_status(
                "Available"
            )
        )
