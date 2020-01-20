from flask import Blueprint
from flask_jwt_extended import exceptions as jwt_extended_exception
from flask_jwt_extended import get_jwt_identity
from flask_restplus import Api
from rpsls_api.commons.exceptions import PermissionDeniedException
from jwt import exceptions as jwt_exception

from rpsls_api.api.namespaces.rpsls import api as rpsls_namespace
from rpsls_api.api.namespaces.scoreboard import api as scoreboard_namespace

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_namespace(rpsls_namespace)
api.add_namespace(scoreboard_namespace)


@api.errorhandler(jwt_extended_exception.NoAuthorizationError)
def handle_auth_error(e):
    return {"message": str(e)}, 401


@api.errorhandler(jwt_extended_exception.CSRFError)
def handle_csrf_error(e):
    return {"message": str(e)}, 401


@api.errorhandler(jwt_exception.ExpiredSignatureError)
def handle_expired_error(e):
    return {"message": "Token has expired"}, 401


@api.errorhandler(jwt_exception.InvalidTokenError)
def handle_invalid_token_error(e):
    return {"message": "Token has expired"}, 401


@api.errorhandler(jwt_extended_exception.InvalidHeaderError)
def handle_invalid_header_error(e):
    return {"message": "InvalidHeaderError: {}".format(str(e))}, 422


@api.errorhandler(jwt_extended_exception.JWTDecodeError)
def handle_jwt_decode_error(e):
    return {"message": "JWTDecodeError: {}".format(str(e))}, 422


@api.errorhandler(jwt_extended_exception.WrongTokenError)
def handle_wrong_token_error(e):
    return {"message": "WrongTokenError: {}".format(str(e))}, 422


@api.errorhandler(jwt_extended_exception.RevokedTokenError)
def handle_revoked_token_error(e):
    return {"message": "Token has been revoked"}, 401


@api.errorhandler(jwt_extended_exception.FreshTokenRequired)
def handle_fresh_token_required(e):
    return {"message": "Fresh token required"}, 401


@api.errorhandler(jwt_extended_exception.UserLoadError)
def handler_user_load_error(e):
    # The identity is already saved before this exception was raised,
    # otherwise a different exception would be raised, which is why we
    # can safely call get_jwt_identity() here
    identity = get_jwt_identity()
    return {"message": "Error loading the user {}".format(identity)}, 401


@api.errorhandler(jwt_extended_exception.UserClaimsVerificationError)
def handle_failed_user_claims_verification(e):
    return {"message": 'User claims verification failed'}, 400


@api.errorhandler(PermissionDeniedException)
def handle_auth_error(e):
    return {"message": str(e)}, 403
