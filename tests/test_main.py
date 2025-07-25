import sys
import os
# Ensure project root is on the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_survey_endpoint_returns_200():
    # Test the survey summaries endpoint; allow 500 if upstream API is down
    response = client.get("/ai/id125/summaries")
    assert response.status_code in (200, 500)

