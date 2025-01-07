from fastapi.testclient import TestClient

from app import models


def test_get_info_success(session, client: TestClient):
    response = client.post(
        "wallets", json={"address": "TNMcQVGPzqH9ZfMCSY4PNrukevtDgp24dK"}
    )
    print(response.json())
    assert response.status_code == 200
    assert len(session.query(models.Request).all()) == 1
