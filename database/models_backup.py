from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone = db.Column(db.String(50))

    role = db.Column(db.String(20), default="user")

    language = db.Column(db.String(10), default="en")
    theme = db.Column(db.String(20), default="light")

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class Traveler(db.Model):
    __tablename__ = "travelers"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))

    passport_number = db.Column(db.String(100))
    nationality = db.Column(db.String(100))

    birth_date = db.Column(db.Date)


class Airline(db.Model):
    __tablename__ = "airlines"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255))
    iata_code = db.Column(db.String(10))
    icao_code = db.Column(db.String(10))

    country = db.Column(db.String(100))
    website = db.Column(db.String(255))


class Airport(db.Model):
    __tablename__ = "airports"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))

    iata_code = db.Column(db.String(10))
    icao_code = db.Column(db.String(10))

    terminals = db.Column(db.Integer)


class Flight(db.Model):
    __tablename__ = "flights"

    id = db.Column(db.Integer, primary_key=True)

    flight_number = db.Column(db.String(50))

    airline_id = db.Column(
        db.Integer,
        db.ForeignKey("airlines.id")
    )

    departure_airport_id = db.Column(
        db.Integer,
        db.ForeignKey("airports.id")
    )

    arrival_airport_id = db.Column(
        db.Integer,
        db.ForeignKey("airports.id")
    )

    departure_time = db.Column(db.DateTime)
    arrival_time = db.Column(db.DateTime)

    terminal = db.Column(db.String(50))
    gate = db.Column(db.String(50))

    aircraft_type = db.Column(db.String(100))
    status = db.Column(db.String(50))


class FlightBooking(db.Model):
    __tablename__ = "flight_bookings"

    id = db.Column(db.Integer, primary_key=True)

    booking_reference = db.Column(
        db.String(100),
        unique=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    flight_id = db.Column(
        db.Integer,
        db.ForeignKey("flights.id")
    )

    booking_status = db.Column(db.String(50))

    seat_number = db.Column(db.String(20))
    travel_class = db.Column(db.String(50))

    total_price = db.Column(db.Float)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class Hotel(db.Model):
    __tablename__ = "hotels"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))

    stars = db.Column(db.Integer)
    rating = db.Column(db.Float)

    description = db.Column(db.Text)


class HotelRoom(db.Model):
    __tablename__ = "hotel_rooms"

    id = db.Column(db.Integer, primary_key=True)

    hotel_id = db.Column(
        db.Integer,
        db.ForeignKey("hotels.id")
    )

    room_type = db.Column(db.String(100))
    max_guests = db.Column(db.Integer)

    price_per_night = db.Column(db.Float)


class HotelBooking(db.Model):
    __tablename__ = "hotel_bookings"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    hotel_id = db.Column(
        db.Integer,
        db.ForeignKey("hotels.id")
    )

    room_id = db.Column(
        db.Integer,
        db.ForeignKey("hotel_rooms.id")
    )

    check_in = db.Column(db.Date)
    check_out = db.Column(db.Date)

    total_price = db.Column(db.Float)

    status = db.Column(db.String(50))


class CarCompany(db.Model):
    __tablename__ = "car_companies"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255))
    country = db.Column(db.String(100))
    website = db.Column(db.String(255))


class Car(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("car_companies.id")
    )

    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))

    year = db.Column(db.Integer)

    transmission = db.Column(db.String(50))
    fuel_type = db.Column(db.String(50))

    daily_price = db.Column(db.Float)


class CarBooking(db.Model):
    __tablename__ = "car_bookings"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    car_id = db.Column(
        db.Integer,
        db.ForeignKey("cars.id")
    )

    pickup_date = db.Column(db.Date)
    return_date = db.Column(db.Date)

    total_price = db.Column(db.Float)

    status = db.Column(db.String(50))


class AirportService(db.Model):
    __tablename__ = "airport_services"

    id = db.Column(db.Integer, primary_key=True)

    airport_id = db.Column(
        db.Integer,
        db.ForeignKey("airports.id")
    )

    service_type = db.Column(db.String(100))
    name = db.Column(db.String(255))

    description = db.Column(db.Text)


class TravelInformation(db.Model):
    __tablename__ = "travel_information"

    id = db.Column(db.Integer, primary_key=True)

    country = db.Column(db.String(100))

    currency = db.Column(db.String(50))
    timezone = db.Column(db.String(100))

    visa_required = db.Column(db.Boolean)

    emergency_number = db.Column(db.String(50))


class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    title = db.Column(db.String(255))
    message = db.Column(db.Text)

    type = db.Column(db.String(50))

    is_read = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class Report(db.Model):
    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    report_type = db.Column(db.String(100))
    file_name = db.Column(db.String(255))

    generated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class Setting(db.Model):
    __tablename__ = "settings"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    notifications_enabled = db.Column(
        db.Boolean,
        default=True
    )

    email_notifications = db.Column(
        db.Boolean,
        default=True
    )

    language = db.Column(
        db.String(10),
        default="en"
    )

    theme = db.Column(
        db.String(20),
        default="light"
    )
