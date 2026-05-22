import pytest
from fastapi.testclient import TestClient

from src.app import app, reset_activities_data


@pytest.fixture(autouse=True)
def reset_activities():
    reset_activities_data()
    yield
    reset_activities_data()


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
