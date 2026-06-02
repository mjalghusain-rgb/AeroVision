from flask import Blueprint
from flask import render_template

from flask_login import (
    login_required
)

from database.models import (
    Flight,
    Airline,
    Airport,
    FlightBooking
)

analytics_bp = Blueprint(
    "analytics",
    __name__,
    url_prefix="/analytics"
)


@analytics_bp.route("/")
@login_required
def analytics_dashboard():

    total_flights = (
        Flight.query.count()
    )

    total_airlines = (
        Airline.query.count()
    )

    total_airports = (
        Airport.query.count()
    )

    total_bookings = (
        FlightBooking.query.count()
    )

    confirmed_bookings = (
        FlightBooking.query.filter_by(
            booking_status="Confirmed"
        ).count()
    )

    cancelled_bookings = (
        FlightBooking.query.filter_by(
            booking_status="Cancelled"
        ).count()
    )

    revenue = sum(
        booking.total_price or 0
        for booking in
        FlightBooking.query.all()
    )

    return render_template(
        "analytics/index.html",
        total_flights=total_flights,
        total_airlines=total_airlines,
        total_airports=total_airports,
        total_bookings=total_bookings,
        confirmed_bookings=confirmed_bookings,
        cancelled_bookings=cancelled_bookings,
        revenue=revenue
    )


@analytics_bp.route("/airlines")
@login_required
def airlines_analytics():

    airlines = (
        Airline.query
        .order_by(
            Airline.name.asc()
        )
        .all()
    )

    return render_template(
        "analytics/airlines.html",
        airlines=airlines
    )


@analytics_bp.route("/airports")
@login_required
def airports_analytics():

    airports = (
        Airport.query
        .order_by(
            Airport.name.asc()
        )
        .all()
    )

    return render_template(
        "analytics/airports.html",
        airports=airports
    )
@analytics_bp.route("/countries")
@login_required
def countries_analytics():

    airlines = Airline.query.all()
    airports = Airport.query.all()

    countries = {}

    for airline in airlines:

        country = (
            airline.country
            or "Unknown"
        )

        countries[country] = (
            countries.get(
                country,
                0
            ) + 1
        )

    for airport in airports:

        country = (
            airport.country
            or "Unknown"
        )

        countries[country] = (
            countries.get(
                country,
                0
            ) + 1
        )

    countries = sorted(
        countries.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return render_template(
        "analytics/countries.html",
        countries=countries
    )


@analytics_bp.route("/cities")
@login_required
def cities_analytics():

    airports = Airport.query.all()

    cities = {}

    for airport in airports:

        city = (
            airport.city
            or "Unknown"
        )

        cities[city] = (
            cities.get(
                city,
                0
            ) + 1
        )

    cities = sorted(
        cities.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return render_template(
        "analytics/cities.html",
        cities=cities
    )
