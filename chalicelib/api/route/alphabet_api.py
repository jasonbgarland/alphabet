import json

from chalice import BadRequestError, Blueprint

from ..service.alphabet import string_contains_alphabet

alphabet_blueprint = Blueprint(__name__)


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
    if alphabet_blueprint.current_request.query_params is None:
        raise BadRequestError("Must include string parameter with string to verify")

    string_to_evaluate = alphabet_blueprint.current_request.query_params.get("string")
    if string_to_evaluate is None:
        raise BadRequestError("Must include string parameter with string to verify")

    contains_alphabet = string_contains_alphabet(string_to_evaluate)
    result = json.dumps(contains_alphabet)

    return result
