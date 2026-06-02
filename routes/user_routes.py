import os
from werkzeug.utils import secure_filename

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import current_app

from flask_login import (
    login_required,
    current_user
)

from database.models import (
    db,
    User
)

user_bp = Blueprint(
    "user",
    __name__,
    url_prefix="/users"
)


@user_bp.route("/profile")
@login_required
def profile():

    return render_template(
        "users/profile.html",
        user=current_user
    )


@user_bp.route(
    "/edit",
    methods=["GET", "POST"]
)
@login_required
def edit_profile():

    if request.method == "POST":

        current_user.first_name = (
            request.form.get(
                "first_name"
            )
        )

        current_user.last_name = (
            request.form.get(
                "last_name"
            )
        )

        current_user.phone = (
            request.form.get(
                "phone"
            )
        )

        current_user.country = (
            request.form.get(
                "country"
            )
        )

        current_user.city = (
            request.form.get(
                "city"
            )
        )

        current_user.bio = (
            request.form.get(
                "bio"
            )
        )

        image = request.files.get(
            "profile_image"
        )

        if image and image.filename:

            filename = secure_filename(
                image.filename
            )

            upload_dir = os.path.join(
                current_app.static_folder,
                "uploads",
                "profile_images"
            )

            os.makedirs(
                upload_dir,
                exist_ok=True
            )

            image.save(
                os.path.join(
                    upload_dir,
                    filename
                )
            )

            current_user.profile_image = (
                filename
            )

        db.session.commit()

        return redirect(
            "/users/profile"
        )

    return render_template(
        "users/edit_profile.html",
        user=current_user
    )


@user_bp.route("/delete-image")
@login_required
def delete_image():

    current_user.profile_image = (
        "default.png"
    )

    db.session.commit()

    return redirect(
        "/users/profile"
    )
