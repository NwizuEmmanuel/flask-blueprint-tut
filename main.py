from flask import render_template, Flask
from app_blueprint.routes import app_blueprint
from admin_blueprint.routes import admin_blueprint

app = Flask(__name__)
app.register_blueprint(app_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


if __name__ == "__main__":
    app.run(debug=True)
