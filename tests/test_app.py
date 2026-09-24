import pytest

from app import app, teams


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        teams.clear()
        yield client
        teams.clear()


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_add_team(client):
    response = client.post(
        "/register",
        data={
            "team_name": "TestTeam",
            "leader_name": "Test User",
            "email": "test@example.com",
            "members": "3",
            "project_idea": "Smart campus application"
        }
    )

    assert response.status_code == 302
    assert len(teams) == 1
    assert teams[0]["team_name"] == "TestTeam"


def test_invalid_email(client):
    response = client.post(
        "/register",
        data={
            "team_name": "TestTeam",
            "leader_name": "Test User",
            "email": "invalid-email",
            "members": "3",
            "project_idea": "Test project"
        }
    )

    assert response.status_code == 400
    assert len(teams) == 0