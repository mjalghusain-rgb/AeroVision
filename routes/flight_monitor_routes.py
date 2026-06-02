from flask import Blueprint
from flask import render_template

from database.models import (
    Flight,
    Airport,
    Airline
)

flight_monitor_bp = Blueprint(
    "flight_monitor",
    __name__,
    url_prefix="/flight-monitor"
)


@flight_monitor_bp.route("/")
def dashboard():

    flights = Flight.query.all()

    airport_stats = {}

    airline_stats = {}

    for flight in flights:

        if flight.departure_airport:

            code = (
                flight.departure_airport.iata_code
                or "Unknown"
            )

            airport_stats[code] = (
                airport_stats.get(
                    code,
                    0
                ) + 1
            )

        if flight.arrival_airport:

            code = (
                flight.arrival_airport.iata_code
                or "Unknown"
            )

            airport_stats[code] = (
                airport_stats.get(
                    code,
                    0
                ) + 1
            )

        if flight.airline:

            airline = (
                flight.airline.name
                or "Unknown"
            )

            airline_stats[airline] = (
                airline_stats.get(
                    airline,
                    0
                ) + 1
            )

    top_airports = sorted(
        airport_stats.items(),
        key=lambda x: x[1],
        reverse=True
    )[:20]

    top_airlines = sorted(
        airline_stats.items(),
        key=lambda x: x[1],
        reverse=True
    )[:20]

    return render_template(
        "flight_monitor/index.html",
        total_flights=Flight.query.count(),
        total_airports=Airport.query.count(),
        total_airlines=Airline.query.count(),
        top_airports=top_airports,
        top_airlines=top_airlines,
        latest_flights=
            Flight.query
            .order_by(
                Flight.id.desc()
            )
            .limit(20)
            .all()
    )
