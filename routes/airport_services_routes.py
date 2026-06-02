from flask import Blueprint
from flask import render_template
from flask import abort

from services.airport_services_service import (
    AirportServicesService
)

airport_services_bp = Blueprint(
    "airport_services",
    __name__,
    url_prefix="/airport-services"
)

airport_services_service = (
    AirportServicesService()
)


@airport_services_bp.route("/")
def airports():

    airports = (
        airport_services_service
        .get_all_airports()
    )

    return render_template(
        "airports/services_index.html",
        airports=airports
    )


@airport_services_bp.route("/<airport_code>")
def airport_services(
    airport_code
):

    services = (
        airport_services_service
        .get_services(
            airport_code
        )
    )

    if not services:
        abort(404)

    return render_template(
        "airports/services.html",
        airport_code=airport_code.upper(),
        services=services
    )
