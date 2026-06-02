import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    APP_NAME = os.getenv(
        "APP_NAME",
        "FlightHub"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change_this_secret_key"
    )

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///flighthub.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEFAULT_LANGUAGE = os.getenv(
        "DEFAULT_LANGUAGE",
        "en"
    )

    DEFAULT_THEME = os.getenv(
        "DEFAULT_THEME",
        "light"
    )

    SUPPORTED_LANGUAGES = [
        "ar",
        "sv",
        "en",
        "ru"
    ]

    SWEDAVIA_API_KEY = os.getenv(
        "SWEDAVIA_API_KEY",
        ""
    )

    SWEDAVIA_API_URL = os.getenv(
        "SWEDAVIA_API_URL",
        ""
    )

    AVIATIONSTACK_API_KEY = os.getenv(
        "AVIATIONSTACK_API_KEY",
        ""
    )

    AVIATIONSTACK_API_URL = os.getenv(
        "AVIATIONSTACK_API_URL",
        "http://api.aviationstack.com/v1"
    )

    WEATHER_API_KEY = os.getenv(
        "WEATHER_API_KEY",
        ""
    )

    WEATHER_API_URL = os.getenv(
        "WEATHER_API_URL",
        ""
    )

    PDF_EXPORT_PATH = os.getenv(
        "PDF_EXPORT_PATH",
        "exports/pdf"
    )

    CSV_EXPORT_PATH = os.getenv(
        "CSV_EXPORT_PATH",
        "exports/csv"
    )

    LOG_FILE = os.getenv(
        "LOG_FILE",
        "logs/application.log"
    )

    ERROR_LOG_FILE = os.getenv(
        "ERROR_LOG_FILE",
        "logs/errors.log"
    )

    SESSION_TIMEOUT = int(
        os.getenv(
            "SESSION_TIMEOUT",
            60
        )
    )

    MAX_SEARCH_RESULTS = int(
        os.getenv(
            "MAX_SEARCH_RESULTS",
            100
        )
    )

    ENABLE_EMAIL_NOTIFICATIONS = (
        os.getenv(
            "ENABLE_EMAIL_NOTIFICATIONS",
            "True"
        ) == "True"
    )

    ENABLE_SYSTEM_NOTIFICATIONS = (
        os.getenv(
            "ENABLE_SYSTEM_NOTIFICATIONS",
            "True"
        ) == "True"
    )

    DEFAULT_CURRENCY = os.getenv(
        "DEFAULT_CURRENCY",
        "SEK"
    )

    TIMEZONE = os.getenv(
        "TIMEZONE",
        "Europe/Stockholm"
    )
