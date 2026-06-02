from flask import Blueprint
from flask import render_template

report_bp = Blueprint(
    "report",
    __name__,
    url_prefix="/reports"
)


@report_bp.route("/")
def reports():
    return render_template(
        "reports/index.html"
    )
