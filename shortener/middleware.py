from functools import wraps
from http import HTTPStatus

from flask import make_response, request
from jose import JWTError, jwt

from config.config import Configuration


def validate_token(f):

    @wraps(f)
    def decorated_fun(*args, **kwargs):
        authorizaition = request.headers.get('authorization')

        if authorizaition is None:
            return make_response("Not valid token provided",
                                 HTTPStatus.UNAUTHORIZED)

        try:
            token_type, token = authorizaition.split(" ")
            payload = jwt.decode(token,
                                 Configuration.TOKEN_KEY,
                                 algorithms=[Configuration.ALGORITHM])

            if not (token_type == "Bearer" and payload["email"]):
                return make_response("Not valid token provided",
                                     HTTPStatus.UNAUTHORIZED)

        except JWTError:
            return make_response("Not valid token provided",
                                 HTTPStatus.UNAUTHORIZED)

        return f(*args, **kwargs)

    return decorated_fun
