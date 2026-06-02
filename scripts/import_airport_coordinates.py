import csv
import sqlite3

DB_PATH = "instance/flighthub.db"
DATASET = "datasets/airports.dat"


def main():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    updated = 0

    with open(
        DATASET,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.reader(
            file
        )

        for row in reader:

            try:

                iata = row[4].strip()

                latitude = float(
                    row[6]
                )

                longitude = float(
                    row[7]
                )

            except Exception:
                continue

            if not iata or iata == "\\N":
                continue

            cursor.execute(
                """
                UPDATE airports
                SET
                    latitude=?,
                    longitude=?
                WHERE
                    iata_code=?
                """,
                (
                    latitude,
                    longitude,
                    iata
                )
            )

            updated += (
                cursor.rowcount
            )

    conn.commit()

    conn.close()

    print(
        f"Updated {updated} airports."
    )


if __name__ == "__main__":
    main()
