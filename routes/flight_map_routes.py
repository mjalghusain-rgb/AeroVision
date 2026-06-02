from flask import Blueprint
from flask import render_template

from database.models import (
    Flight
)

flight_map_bp = Blueprint(
    "flight_map",
    __name__,
    url_prefix="/flight-map"
)


@flight_map_bp.route("/")
def flight_map():

    flights = (
        Flight.query
        .all()
    )

    routes = []

    for flight in flights:

        dep = flight.departure_airport
        arr = flight.arrival_airport

        if not dep or not arr:
            continue

        if (
            dep.latitude is None
            or dep.longitude is None
            or arr.latitude is None
            or arr.longitude is None
        ):
            continue

        routes.append({

            "flight":
                flight.flight_number,

            "departure":
                dep.name,

            "arrival":
                arr.name,

            "dep_lat":
                dep.latitude,

            "dep_lon":
                dep.longitude,

            "arr_lat":
                arr.latitude,

            "arr_lon":
                arr.longitude

        })

    return render_template(
        "flight_map/index.html",
        routes=routes
    )
