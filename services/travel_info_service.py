from data.travel_info import TRAVEL_INFO


class TravelInfoService:

    def __init__(self):

        self.travel_info = TRAVEL_INFO

    def get_all_countries(self):

        return self.travel_info

    def get_country(
        self,
        country_name
    ):

        country_name = (
            country_name.lower()
        )

        for country in self.travel_info:

            if (
                country["country"].lower()
                == country_name
            ):

                return country

        return None

    def search(
        self,
        query
    ):

        query = query.lower()

        results = []

        for country in self.travel_info:

            if (

                query in country["country"].lower()

                or

                query in country["capital"].lower()

                or

                query in country["currency"].lower()

                or

                query in country["language"].lower()

            ):

                results.append(
                    country
                )

        return results

    def total_countries(self):

        return len(
            self.travel_info
        )

    def get_currencies(self):

        currencies = set()

        for country in self.travel_info:

            currencies.add(
                country["currency"]
            )

        return sorted(
            list(currencies)
        )

    def get_languages(self):

        languages = set()

        for country in self.travel_info:

            languages.add(
                country["language"]
            )

        return sorted(
            list(languages)
        )
