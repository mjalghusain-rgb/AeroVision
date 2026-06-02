from flask import Blueprint
from flask import render_template
from flask import request
from flask import abort

from services.car_service import (
    CarService
)

car_bp = Blueprint(
    "car",
    __name__,
    url_prefix="/cars"
)

car_service = CarService()


@car_bp.route("/")
def cars():

    cars = (
        car_service
        .get_all_cars()
    )

    return render_template(
        "cars/index.html",
        cars=cars
    )


@car_bp.route("/details/<car_id>")
def car_details(
    car_id
):

    car = (
        car_service
        .get_car_by_id(
            car_id
        )
    )

    if not car:
        abort(404)

    return render_template(
        "cars/details.html",
        car=car
    )


@car_bp.route("/search")
def car_search():

    query = request.args.get(
        "q",
        ""
    )

    cars = []

    if query:

        cars = (
            car_service.search(
                query
            )
        )

    return render_template(
        "cars/search.html",
        cars=cars,
        query=query
    )
