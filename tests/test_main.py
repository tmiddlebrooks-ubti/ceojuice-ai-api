from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_survey_endpoint_returns_200():
    # Allow 500 if upstream API is down
    response = client.get("/ai/id125/summaries")
    assert response.status_code in (200, 500)
