"""
And to end / API tests for the alphabet API
"""
import urllib

from api.service.test.test_alphabet import generate_random_str, ALPHABET_STRING
class TestAlphabet:
    def test_string_contains_alphabet_returns_true(self, client):
        test_string = "11!lmnopqrstuvwXYZabcdefghijk\u03A9\n"
        expected_response = "true"

        response = client.get(f"/alphabet?string={test_string}")

        assert response.status_code == 200
        assert response.text == expected_response

    def test_string_contains_alphabet_large_string_returns_true(self, client):
        test_string = generate_random_str(1000) + ALPHABET_STRING # ensure string always includes the required characters
        expected_response = "true"

        response = client.get(f"/alphabet?string={urllib.parse.quote_plus(test_string)}")

        assert response.status_code == 200
        assert response.text == expected_response

    def test_string_empty_returns_false(self, client):
        test_string = ""
        expected_response = "false"

        response = client.get(f"/alphabet?string={test_string}")

        assert response.status_code == 200
        assert response.text == expected_response

    def test_string_does_not_contain_full_alphabet_returns_false(self, client):
        test_string = "abcdefg"
        expected_response = "false"

        response = client.get(f"/alphabet?string={test_string}")

        assert response.status_code == 200
        assert response.text == expected_response

    def test_missing_string_parameter_returns_400(self, client):
        expected_response = {'error': 'Must include string parameter with string to verify',
                             'message': 'Invalid request'}

        response = client.get("/alphabet")

        assert response.status_code == 400
        assert response.json == expected_response
