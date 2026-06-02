from flask import Blueprint
from flask import render_template
from flask import abort
from flask import request

from database.models import (
    Airport,
    Flight
)

airport_bp = Blueprint(
    "airport",
    __name__,
    url_prefix="/airports"
)


@airport_bp.route("/")
def airports():

    search = request.args.get(
        "search",
        ""
    )

    page = request.args.get(
        "page",
        1,
        type=int
    )

    query = Airport.query

    if search:

        query = query.filter(

            Airport.name.contains(
                search
            )

            |

            Airport.city.contains(
                search
            )

            |

            Airport.country.contains(
                search
            )

            |

            Airport.iata_code.contains(
                search
            )

            |

            Airport.icao_code.contains(
                search
            )

        )

    airports = (
        query
        .order_by(
            Airport.name.asc()
        )
        .paginate(
            page=page,
            per_page=25,
            error_out=False
        )
    )

    return render_template(
        "airports/index.html",
        airports=airports,
        search=search
    )


@airport_bp.route("/<airport_code>")
def airport_details(
    airport_code
):

    airport = (
        Airport.query
        .filter_by(
            iata_code=airport_code.upper()
        )
        .first()
    )

    if not airport:
        abort(404)

    departures = (
        Flight.query
        .filter_by(
            departure_airport_id=airport.id
        )
        .all()
    )

    arrivals = (
        Flight.query
        .filter_by(
            arrival_airport_id=airport.id
        )
        .all()
    )

    return render_template(
        "airports/details.html",
        airport=airport,
        departures=departures,
        arrivals=arrivals
    )
