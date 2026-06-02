from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import (
    login_user,
    logout_user,
    current_user
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from database.models import (
    db,
    User
)

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth_bp.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if current_user.is_authenticated:

        return redirect("/")

    if request.method == "POST":

        username = request.form.get(
            "username"
        )

        email = request.form.get(
            "email"
        )

        password = request.form.get(
            "password"
        )

        existing_user = (
            User.query.filter_by(
                email=email
            ).first()
        )

        if existing_user:

            flash(
                "Email already exists.",
                "danger"
            )

            return redirect(
                url_for(
                    "auth.register"
                )
            )

        user = User(

            username=username,

            email=email,

            password_hash=generate_password_hash(
                password
            ),

            role="user"

        )

        db.session.add(
            user
        )

        db.session.commit()

        flash(
            "Account created successfully.",
            "success"
        )

        return redirect(
            url_for(
                "auth.login"
            )
        )

    return render_template(
        "auth/register.html"
    )


@auth_bp.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if current_user.is_authenticated:

        return redirect("/")

    if request.method == "POST":

        email = request.form.get(
            "email"
        )

        password = request.form.get(
            "password"
        )

        user = (
            User.query.filter_by(
                email=email
            ).first()
        )

        if (
            user
            and
            check_password_hash(
                user.password_hash,
                password
            )
        ):

            login_user(
                user
            )

            return redirect(
                "/"
            )

        flash(
            "Invalid email or password.",
            "danger"
        )

    return render_template(
        "auth/login.html"
    )


@auth_bp.route("/logout")
def logout():

    logout_user()

    return redirect(
        url_for(
            "auth.login"
        )
    )
