import json

from flask import Blueprint, request, make_response
from werkzeug.exceptions import BadRequest

from ..service.alphabet import string_contains_alphabet

alphabet_blueprint = Blueprint("alphabet", __name__)


@alphabet_blueprint.route("/alphabet", methods=["GET"])
def alphabet():
    """
    Determine whether the passed in string contains every letter of the alphabet. This is a case insensitive search.
    Numbers, special characters, and whitespace are OK.
    ---
    tags:
        - Alphabet
    parameters:
      - name: string
        in: query
        schema:
            type: string
        description: The string to check
        required: true
        default: the quick brown fox jumps over the lazy dog
    responses:
      200:
        description: True if the string contains every letter of the alphabet, false if it does not.
        content:
          text/plain:
            schema:
              type: string
    """
    string_to_evaluate = request.args.get("string")
    if string_to_evaluate is None:
        response_dict = {
            "message": "Invalid request",
            "error": "Must include string parameter with string to verify",
        }
        response = make_response(response_dict, 400)
        raise BadRequest("description", response)

    contains_alphabet = string_contains_alphabet(string_to_evaluate)
    result = json.dumps(contains_alphabet)

    return result, 200
