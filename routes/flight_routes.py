from flask import Blueprint
from flask import render_template
from flask import abort
from flask import request

from services.flight_service import (
    FlightService
)

from services.aviationstack_service import (
    AviationStackService
)

flight_bp = Blueprint(
    "flight",
    __name__,
    url_prefix="/flights"
)

flight_service = FlightService()

aviation_service = (
    AviationStackService()
)


@flight_bp.route("/")
def flights():

    flights = (
        flight_service
        .get_all_flights()
    )

    return render_template(
        "flights/index.html",
        flights=flights
    )


@flight_bp.route("/live")
def live_flights():

    try:

        data = (
            aviation_service
            .get_flights(20)
        )

        flights = (
            data.get(
                "data",
                []
            )
        )

    except Exception:

        flights = []

    return render_template(
        "flights/live.html",
        flights=flights
    )


@flight_bp.route("/search")
def flight_search():

    query = request.args.get(
        "q",
        ""
    )

    flights = []

    if query:

        try:

            flights = (
                aviation_service
                .search_flights(
                    query
                )
            )

        except Exception:

            flights = []

    return render_template(
        "flights/search.html",
        flights=flights,
        query=query
    )


@flight_bp.route("/details/<flight_number>")
def flight_details(
    flight_number
):

    flight = (
        flight_service
        .get_flight_by_number(
            flight_number
        )
    )

    if not flight:
        abort(404)

    return render_template(
        "flights/details.html",
        flight=flight
    )


@flight_bp.route("/arrivals")
def arrivals():

    flights = (
        flight_service
        .get_arrivals("ARN")
    )

    return render_template(
        "flights/arrivals.html",
        flights=flights
    )


@flight_bp.route("/departures")
def departures():

    flights = (
        flight_service
        .get_departures("ARN")
    )

    return render_template(
        "flights/departures.html",
        flights=flights
    )
