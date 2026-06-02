from flask import Blueprint
from flask import render_template
from flask import request
from flask import abort

from services.notification_service import (
    NotificationService
)

notification_bp = Blueprint(
    "notification",
    __name__,
    url_prefix="/notifications"
)

notification_service = (
    NotificationService()
)


@notification_bp.route("/")
def notifications():

    notifications = (
        notification_service
        .get_all_notifications()
    )

    return render_template(
        "notifications/index.html",
        notifications=notifications
    )


@notification_bp.route("/details/<notification_id>")
def notification_details(
    notification_id
):

    notification = (
        notification_service
        .get_notification_by_id(
            notification_id
        )
    )

    if not notification:
        abort(404)

    return render_template(
        "notifications/details.html",
        notification=notification
    )


@notification_bp.route("/search")
def notification_search():

    query = request.args.get(
        "q",
        ""
    )

    notifications = []

    if query:

        notifications = (
            notification_service.search(
                query
            )
        )

    return render_template(
        "notifications/search.html",
        notifications=notifications,
        query=query
    )
