from http import HTTPStatus

from flask import jsonify, make_response, redirect, request
from marshmallow import ValidationError

from config.extensions import db
from middleware import validate_token
from models import Link
from schemas import link_schema, links_schema


@validate_token
def add_link():
    request_data = request.get_json()

    try:
        link_data = link_schema.load(request_data)
    except ValidationError as err:
        return make_response(jsonify(err.messages), HTTPStatus.BAD_REQUEST)

    link = Link(**link_data)
    db.session.add(link)
    db.session.commit()

    return make_response(link_schema.jsonify(link), HTTPStatus.CREATED)


@validate_token
def check_code(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    return make_response(link_schema.jsonify(link), HTTPStatus.OK)


@validate_token
def stats():
    links = Link.query.all()
    return make_response(jsonify(links_schema.dump(links)), HTTPStatus.OK)


def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()

    link.visits = link.visits + 1
    db.session.commit()

    return redirect(link.original_url)
