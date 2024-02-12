from flask import render_template, Blueprint

admin_blueprint = Blueprint("admin_blueprint", __name__, template_folder="templates")


@admin_blueprint.route("/")
def admin_index():
    return render_template("admin_index.html")


@admin_blueprint.route("/signin")
def sign_in():
    return render_template("signin.html")


@admin_blueprint.route("/signup")
def sign_up():
    return render_template("signup.html")
