from flask import Blueprint
from flask import render_template
from flask import request
from flask import abort

from services.travel_info_service import (
    TravelInfoService
)

travel_bp = Blueprint(
    "travel",
    __name__,
    url_prefix="/travel"
)

travel_service = (
    TravelInfoService()
)


@travel_bp.route("/")
def travel_home():

    countries = (
        travel_service
        .get_all_countries()
    )

    return render_template(
        "travel/index.html",
        countries=countries
    )


@travel_bp.route("/details/<country>")
def travel_details(
    country
):

    country_info = (
        travel_service
        .get_country(
            country
        )
    )

    if not country_info:
        abort(404)

    return render_template(
        "travel/details.html",
        country=country_info
    )


@travel_bp.route("/search")
def travel_search():

    query = request.args.get(
        "q",
        ""
    )

    countries = []

    if query:

        countries = (
            travel_service
            .search(
                query
            )
        )

    return render_template(
        "travel/search.html",
        countries=countries,
        query=query
    )
