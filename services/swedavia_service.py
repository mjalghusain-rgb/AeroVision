import os
import requests
from datetime import datetime


class SwedaviaService:

    def __init__(self):

        self.api_key = os.getenv(
            "SWEDAVIA_API_KEY",
            ""
        )

        self.base_url = (
            "https://api.swedavia.se/flightinfo/v2"
        )

        self.headers = {
            "Accept": "application/json",
            "Ocp-Apim-Subscription-Key": self.api_key
        }

    def get_arrivals(
        self,
        airport_iata="ARN",
        date=None
    ):

        if not date:
            date = datetime.now().strftime(
                "%Y-%m-%d"
            )

        url = (
            f"{self.base_url}/"
            f"{airport_iata}/"
            f"arrivals/"
            f"{date}"
        )

        try:

            response = requests.get(
                url,
                headers=self.headers,
                timeout=20
            )

            response.raise_for_status()

            return response.json()

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    def get_departures(
        self,
        airport_iata="ARN",
        date=None
    ):

        if not date:
            date = datetime.now().strftime(
                "%Y-%m-%d"
            )

        url = (
            f"{self.base_url}/"
            f"{airport_iata}/"
            f"departures/"
            f"{date}"
        )

        try:

            response = requests.get(
                url,
                headers=self.headers,
                timeout=20
            )

            response.raise_for_status()

            return response.json()

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    def health_check(self):

        try:

            data = self.get_arrivals()

            if isinstance(data, dict):
                return True

            return False

        except Exception:

            return False
