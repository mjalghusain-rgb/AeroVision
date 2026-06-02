from database.models import (
    db,
    Airport
)

from data.airport_reference import (
    AIRPORT_REFERENCE
)


class AirportEnrichmentService:

    def enrich_airports(self):

        updated = 0

        airports = Airport.query.all()

        for airport in airports:

            code = (
                airport.iata_code
                or ""
            ).upper()

            if code not in AIRPORT_REFERENCE:
                continue

            airport.city = (
                AIRPORT_REFERENCE[code]["city"]
            )

            airport.country = (
                AIRPORT_REFERENCE[code]["country"]
            )

            updated += 1

        db.session.commit()

        return updated
