from database.db import create_app

from routes.language_routes import (
    language_bp
)

from routes.flight_map_routes import (
    flight_map_bp
)

from routes.home_routes import home_bp
from routes.flight_routes import flight_bp
from routes.dashboard_routes import dashboard_bp
from routes.booking_routes import booking_bp
from routes.hotel_routes import hotel_bp
from routes.car_routes import car_bp
from routes.airport_routes import airport_bp

from routes.airport_services_routes import (
    airport_services_bp
)

from routes.analytics_routes import (
    analytics_bp
)

from routes.flight_monitor_routes import (
    flight_monitor_bp
)

from routes.travel_routes import (
    travel_bp
)

from routes.notification_routes import (
    notification_bp
)

from routes.report_routes import (
    report_bp
)

from routes.settings_routes import (
    settings_bp
)

from routes.auth_routes import (
    auth_bp
)

from routes.admin_routes import (
    admin_bp
)

from routes.user_routes import (
    user_bp
)

app = create_app()

app.register_blueprint(
    language_bp
)

app.register_blueprint(
    home_bp
)

app.register_blueprint(
    flight_bp
)

app.register_blueprint(
    dashboard_bp
)

app.register_blueprint(
    booking_bp
)

app.register_blueprint(
    hotel_bp
)

app.register_blueprint(
    car_bp
)

app.register_blueprint(
    airport_bp
)

app.register_blueprint(
    airport_services_bp
)

app.register_blueprint(
    analytics_bp
)

app.register_blueprint(
    travel_bp
)

app.register_blueprint(
    notification_bp
)

app.register_blueprint(
    report_bp
)

app.register_blueprint(
    settings_bp
)

app.register_blueprint(
    auth_bp
)

app.register_blueprint(
    flight_monitor_bp
)

app.register_blueprint(
    admin_bp
)

app.register_blueprint(
    flight_map_bp
)

app.register_blueprint(
    user_bp
)

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
