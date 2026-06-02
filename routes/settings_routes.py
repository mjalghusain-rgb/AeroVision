from flask import Blueprint
from flask import render_template

settings_bp = Blueprint(
    "settings",
    __name__,
    url_prefix="/settings"
)


@settings_bp.route("/")
def settings():
    return render_template(
        "settings/index.html"
    )
