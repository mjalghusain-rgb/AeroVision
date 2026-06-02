from data.cars import CARS


class CarService:

    def __init__(self):

        self.cars = CARS

    def get_all_cars(self):

        return self.cars

    def get_car_by_id(
        self,
        car_id
    ):

        car_id = car_id.upper()

        for car in self.cars:

            if (
                car["car_id"]
                == car_id
            ):

                return car

        return None

    def search(
        self,
        query
    ):

        query = query.lower()

        results = []

        for car in self.cars:

            if (

                query in car["car_id"].lower()

                or

                query in car["brand"].lower()

                or

                query in car["model"].lower()

                or

                query in car["category"].lower()

                or

                query in car["airport"].lower()

                or

                query in car["status"].lower()

            ):

                results.append(
                    car
                )

        return results

    def get_by_airport(
        self,
        airport
    ):

        airport = airport.upper()

        results = []

        for car in self.cars:

            if (
                car["airport"]
                == airport
            ):

                results.append(
                    car
                )

        return results

    def get_by_status(
        self,
        status
    ):

        status = status.lower()

        results = []

        for car in self.cars:

            if (
                car["status"].lower()
                == status
            ):

                results.append(
                    car
                )

        return results

    def total_cars(self):

        return len(
            self.cars
        )

    def available_cars(self):

        return len(
            self.get_by_status(
                "Available"
            )
        )
