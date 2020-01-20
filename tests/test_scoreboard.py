import json
from unittest.mock import patch


def test_scoreboard_valid_result(client):
    res = client.post(
        "/api/v1/scoreboard",
        json={'username': 'ella', 'result': 'win'},
    )

    assert json.loads(res.data).get("error") is None


def test_scoreboard_invalid_result(client):
    res = client.post(
        "/api/v1/scoreboard",
        json={'username': 'ella', 'result': 'invalid'},
    )

    assert json.loads(res.data).get("error") == "Result not valid."
