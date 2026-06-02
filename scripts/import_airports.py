import csv
import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from database.db import create_app
from database.models import (
    db,
    Airport
)


def import_airports():

    app = create_app()

    with app.app_context():

        file_path = (
            "datasets/airports.dat"
        )

        added = 0
        skipped = 0

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.reader(file)

            for row in reader:

                if len(row) < 8:
                    continue

                name = row[1].strip()
                city = row[2].strip()
                country = row[3].strip()
                iata = row[4].strip()
                icao = row[5].strip()

                if (
                    not iata
                    or
                    iata == "\\N"
                ):
                    continue

                exists = (
                    Airport.query
                    .filter_by(
                        iata_code=iata
                    )
                    .first()
                )

                if exists:

                    skipped += 1
                    continue

                airport = Airport(

                    name=name,

                    city=city,

                    country=country,

                    iata_code=iata,

                    icao_code=icao,

                    terminals=1

                )

                db.session.add(
                    airport
                )

                added += 1

                if added % 500 == 0:

                    db.session.commit()

                    print(
                        f"Imported {added}"
                    )

        db.session.commit()

        print()
        print(
            f"Added: {added}"
        )

        print(
            f"Skipped: {skipped}"
        )


if __name__ == "__main__":

    import_airports()
