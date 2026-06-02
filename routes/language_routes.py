from flask import (
    Blueprint,
    session,
    redirect,
    request
)

from config import Config

language_bp = Blueprint(
    "language",
    __name__,
    url_prefix="/language"
)


@language_bp.route("/<lang>")
def change_language(lang):

    if lang in Config.SUPPORTED_LANGUAGES:

        session["language"] = lang

    return redirect(

        request.referrer
        or "/"

    )
