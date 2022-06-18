from flask import Flask

from config.extensions import db, ma
from routers import app_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.config.Configuration")

    app.register_blueprint(app_routes)
    db.init_app(app)
    ma.init_app(app)

    return app


if __name__ == "__main__":
    server = create_app()
    server.run(host="0.0.0.0")
