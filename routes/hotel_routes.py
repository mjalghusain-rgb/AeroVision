from flask import Blueprint
from flask import render_template
from flask import request
from flask import abort

from services.hotel_service import (
    HotelService
)

hotel_bp = Blueprint(
    "hotel",
    __name__,
    url_prefix="/hotels"
)

hotel_service = HotelService()


@hotel_bp.route("/")
def hotels():

    hotels = (
        hotel_service
        .get_all_hotels()
    )

    return render_template(
        "hotels/index.html",
        hotels=hotels
    )


@hotel_bp.route("/details/<hotel_id>")
def hotel_details(
    hotel_id
):

    hotel = (
        hotel_service
        .get_hotel_by_id(
            hotel_id
        )
    )

    if not hotel:
        abort(404)

    return render_template(
        "hotels/details.html",
        hotel=hotel
    )


@hotel_bp.route("/search")
def hotel_search():

    query = request.args.get(
        "q",
        ""
    )

    hotels = []

    if query:

        hotels = (
            hotel_service.search(
                query
            )
        )

    return render_template(
        "hotels/search.html",
        hotels=hotels,
        query=query
    )

