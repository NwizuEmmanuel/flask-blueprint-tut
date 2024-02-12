from flask import render_template, Blueprint

app_blueprint = Blueprint("app_blueprint", __name__, template_folder="templates")


@app_blueprint.route("/")
def index():
    return render_template("index.html")


@app_blueprint.route("/test")
def test():
    return render_template("test.html")
