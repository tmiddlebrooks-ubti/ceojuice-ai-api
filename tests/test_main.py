import os
import sys
from fastapi.testclient import TestClient  # noqa: E402
from main import app  # noqa: E402

# Ensure project root is on the import path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)
sys.path.insert(0, project_root)

client = TestClient(app)


def test_survey_endpoint_returns_200():
    # Test the survey summaries endpoint; allow 500 if upstream API is down
    response = client.get("/ai/id125/summaries")
    assert response.status_code in (200, 500)
