class AirportService:

    def __init__(self):

        self.airports = [

            {
                "iata": "ARN",
                "name": "Stockholm Arlanda Airport",
                "city": "Stockholm",
                "country": "Sweden",
                "address": "190 45 Stockholm-Arlanda, Sweden",
                "latitude": 59.6519,
                "longitude": 17.9186,
                "terminals": 4,
                "website": "https://www.swedavia.com/arlanda/",
                "phone": "+46 10 109 10 00",
                "email": "info@swedavia.se",
                "runways": 3,
                "airlines": 45,
                "flights_today": 500,
                "services": [
                    "Lounges",
                    "Restaurants",
                    "Shops",
                    "Parking",
                    "Taxi",
                    "Bus",
                    "Train"
                ]
            },

            {
                "iata": "BMA",
                "name": "Stockholm Bromma Airport",
                "city": "Stockholm",
                "country": "Sweden",
                "address": "Bromma Airport, 168 67 Bromma, Sweden",
                "latitude": 59.3544,
                "longitude": 17.9417,
                "terminals": 1,
                "website": "https://www.swedavia.com/bromma/",
                "phone": "+46 10 109 40 00",
                "email": "info@swedavia.se",
                "runways": 1,
                "airlines": 8,
                "flights_today": 60,
                "services": [
                    "Restaurants",
                    "Parking",
                    "Taxi",
                    "Bus"
                ]
            },

            {
                "iata": "GOT",
                "name": "Göteborg Landvetter Airport",
                "city": "Göteborg",
                "country": "Sweden",
                "address": "438 80 Landvetter, Sweden",
                "latitude": 57.6628,
                "longitude": 12.2798,
                "terminals": 1,
                "website": "https://www.swedavia.com/landvetter/",
                "phone": "+46 10 109 31 00",
                "email": "info@swedavia.se",
                "runways": 1,
                "airlines": 25,
                "flights_today": 180,
                "services": [
                    "Lounges",
                    "Restaurants",
                    "Shops",
                    "Parking",
                    "Taxi",
                    "Bus"
                ]
            },

            {
                "iata": "MMX",
                "name": "Malmö Airport",
                "city": "Malmö",
                "country": "Sweden",
                "address": "230 32 Malmö-Sturup, Sweden",
                "latitude": 55.5363,
                "longitude": 13.3762,
                "terminals": 1,
                "website": "https://www.swedavia.com/malmo/",
                "phone": "+46 10 109 45 00",
                "email": "info@swedavia.se",
                "runways": 1,
                "airlines": 12,
                "flights_today": 70,
                "services": [
                    "Restaurants",
                    "Parking",
                    "Taxi",
                    "Bus"
                ]
            },

            {
                "iata": "LLA",
                "name": "Luleå Airport",
                "city": "Luleå",
                "country": "Sweden",
                "address": "972 54 Luleå, Sweden",
                "latitude": 65.5438,
                "longitude": 22.1220,
                "terminals": 1,
                "website": "https://www.swedavia.com/lulea/",
                "phone": "+46 10 109 50 00",
                "email": "info@swedavia.se",
                "runways": 1,
                "airlines": 6,
                "flights_today": 40,
                "services": [
                    "Restaurant",
                    "Parking",
                    "Taxi",
                    "Bus"
                ]
            },

            {
                "iata": "UME",
                "name": "Umeå Airport",
                "city": "Umeå",
                "country": "Sweden",
                "address": "904 22 Umeå, Sweden",
                "latitude": 63.7928,
                "longitude": 20.2828,
                "terminals": 1,
                "website": "https://www.swedavia.com/umea/",
                "phone": "+46 10 109 46 00",
                "email": "info@swedavia.se",
                "runways": 1,
                "airlines": 5,
                "flights_today": 35,
                "services": [
                    "Restaurant",
                    "Parking",
                    "Taxi",
                    "Bus"
                ]
            },

            {
                "iata": "VBY",
                "name": "Visby Airport",
                "city": "Visby",
                "country": "Sweden",
                "address": "621 41 Visby, Sweden",
                "latitude": 57.6628,
                "longitude": 18.3462,
                "terminals": 1,
                "website": "https://www.swedavia.com/visby/",
                "phone": "+46 10 109 47 00",
                "email": "info@swedavia.se",
                "runways": 1,
                "airlines": 4,
                "flights_today": 20,
                "services": [
                    "Restaurant",
                    "Parking",
                    "Taxi"
                ]
            }

        ]

    def get_all_airports(self):
        return self.airports

    def get_airport_by_iata(self, airport_code):

        airport_code = airport_code.upper()

        for airport in self.airports:
            if airport["iata"] == airport_code:
                return airport

        return None

    def airport_exists(self, airport_code):

        return (
            self.get_airport_by_iata(airport_code)
            is not None
        )

    def total_airports(self):
        return len(self.airports)
