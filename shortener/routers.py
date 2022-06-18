from flask import Blueprint

from views import add_link, check_code, redirect_to_url, stats

app_routes = Blueprint("app", __name__, url_prefix="/")

app_routes.add_url_rule("/api/stats/", view_func=stats,
                        methods=["GET"])

app_routes.add_url_rule("/api/check/<short_url>", view_func=check_code,
                        methods=["GET"])

app_routes.add_url_rule("/api/link/", view_func=add_link,
                        methods=["POST"])

app_routes.add_url_rule("/<short_url>", view_func=redirect_to_url,
                        methods=["GET"])
