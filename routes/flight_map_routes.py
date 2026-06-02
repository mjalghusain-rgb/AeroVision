from flask import Blueprint
from flask import render_template

from database.models import (
    Flight,
    Airport
)

flight_map_bp = Blueprint(
    "flight_map",
    __name__,
    url_prefix="/flight-map"
)


@flight_map_bp.route("/")
def flight_map():

    airports = (
        Airport.query
        .filter(
            Airport.latitude.isnot(None)
        )
        .filter(
            Airport.longitude.isnot(None)
        )
        .limit(1000)
        .all()
    )

    airport_data = []

    for airport in airports:

        departures = (
            Flight.query
            .filter_by(
                departure_airport_id=airport.id
            )
            .count()
        )

        arrivals = (
            Flight.query
            .filter_by(
                arrival_airport_id=airport.id
            )
            .count()
        )

        airport_data.append({

            "id":
                airport.id,

            "name":
                airport.name,

            "iata":
                airport.iata_code or "",

            "city":
                airport.city or "",

            "country":
                airport.country or "",

            "lat":
                airport.latitude,

            "lon":
                airport.longitude,

            "departures":
                departures,

            "arrivals":
                arrivals

        })

    route_data = []

    flights = Flight.query.all()

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

        route_data.append({

            "flight":
                flight.flight_number,

            "dep_airport":
                dep.iata_code,

            "arr_airport":
                arr.iata_code,

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
        airports=airport_data,
        routes=route_data,
        airport_count=len(airport_data),
        flight_count=len(route_data)
    )
