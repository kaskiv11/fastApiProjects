from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_upload_valid_file():
    with open("tests/zombie.jpg", "rb") as f:
        response = client.post(
            "/upload-image",
            files={'file': ('zombie.jpg', f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert "filename" in response.json()
    assert "file_path" in response.json()


def test_upload_invalid_file():
    with open("tests/text.txt", "rb") as f:
        response = client.post(
            "/upload-image",
            files={'file': ('text.txt', f, "text/plain")}
        )
    assert response.status_code == 400
    assert "Invalid file type." in response.json()["detail"]


def test_upload_file_too_large():
    large_file_content = b"A" * (5*1024*1024+1)
    with open("tests/large_file.jpg", "wb") as f:
        f.write(large_file_content)

    with open("tests/large_file.jpg", "rb") as f:
        response = client.post(
            "/upload-image",
            files={'file': ('large_file.jpg', f, "image/jpeg")}
        )
    assert response.status_code == 413
    assert "File is too large." in response.json()["detail"]


