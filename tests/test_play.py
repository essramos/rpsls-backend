import json
from unittest.mock import patch


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_rock_lizard(computer_choice_mock, client):
    # user plays rock against computer lizard
    computer_choice_mock.return_value = 5
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 1, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "win"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_rock_paper(computer_choice_mock, client):
    # user plays rock against computer paper
    computer_choice_mock.return_value = 2
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 1, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "lose"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_rock_scissor(computer_choice_mock, client):
    # user plays rock against computer paper
    computer_choice_mock.return_value = 3
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 1, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "win"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_rock_spock(computer_choice_mock, client):
    # user plays rock against computer paper
    computer_choice_mock.return_value = 4
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 1, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "lose"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_rock_rock(computer_choice_mock, client):
    # user plays rock against computer rock
    computer_choice_mock.return_value = 1
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 1, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "tie"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_paper_rock(computer_choice_mock, client):
    # user plays paper against computer rock
    computer_choice_mock.return_value = 1
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 2, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "win"



@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_paper_paper(computer_choice_mock, client):
    # user plays paper against computer rock
    computer_choice_mock.return_value = 2
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 2, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "tie"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_paper_scissor(computer_choice_mock, client):
    # user plays paper against computer paper
    computer_choice_mock.return_value = 3
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 2, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "lose"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_paper_spock(computer_choice_mock, client):
    # user plays paper against computer spock
    computer_choice_mock.return_value = 4
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 2, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "win"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_paper_lizard(computer_choice_mock, client):
    # user plays paper against computer lizard
    computer_choice_mock.return_value = 5
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 2, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "lose"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_scissor_rock(computer_choice_mock, client):
    # user plays scissor against computer rock
    computer_choice_mock.return_value = 1
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 3, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "lose"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_scissor_paper(computer_choice_mock, client):
    # user plays scissor against computer paper
    computer_choice_mock.return_value = 2
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 3, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "win"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_scissor_scissor(computer_choice_mock, client):
    # user plays scissor against computer scissor
    computer_choice_mock.return_value = 3
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 3, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "tie"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_scissor_spock(computer_choice_mock, client):
    # user plays scissor against computer spock
    computer_choice_mock.return_value = 4
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 3, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "lose"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_scissor_lizard(computer_choice_mock, client):
    # user plays scissor against computer lizard
    computer_choice_mock.return_value = 5
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 3, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "win"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_spock_rock(computer_choice_mock, client):
    # user plays spock against computer rock
    computer_choice_mock.return_value = 1
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 4, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "win"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_spock_paper(computer_choice_mock, client):
    # user plays spock against computer paper
    computer_choice_mock.return_value = 2
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 4, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "lose"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_spock_scissor(computer_choice_mock, client):
    # user plays spock against computer scissor
    computer_choice_mock.return_value = 3
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 4, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "win"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_spock_spock(computer_choice_mock, client):
    # user plays spock against computer spock
    computer_choice_mock.return_value = 4
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 4, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "tie"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_spock_lizard(computer_choice_mock, client):
    # user plays spock against computer lizard
    computer_choice_mock.return_value = 5
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 4, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "lose"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_lizard_rock(computer_choice_mock, client):
    # user plays spock against computer rock
    computer_choice_mock.return_value = 1
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 5, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "lose"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_lizard_paper(computer_choice_mock, client):
    # user plays spock against computer paper
    computer_choice_mock.return_value = 2
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 5, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "win"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_lizard_scissor(computer_choice_mock, client):
    # user plays spock against computer scissor
    computer_choice_mock.return_value = 3
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 5, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "lose"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_lizard_spock(computer_choice_mock, client):
    # user plays spock against computer spock
    computer_choice_mock.return_value = 4
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 5, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "win"


@patch('rpsls_api.api.namespaces.rpsls.choice_helper.generate_computer_choice')
def test_lizard_lizard(computer_choice_mock, client):
    # user plays spock against computer lizard
    computer_choice_mock.return_value = 5
    res = client.post(
        "/api/v1/rpsls/play",
        json={'player': 5, 'username': 'test'},
    )

    assert json.loads(res.data).get("results") == "tie"