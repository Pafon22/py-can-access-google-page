import pytest
import app.main as main


@pytest.mark.parametrize(
    "result_valid_url, result_has_internet, result_can_access",
    [
        (True, True, "Accessible")
    ]
)
def test_can_access_google_page(
    monkeypatch, result_valid_url, result_has_internet, result_can_access
    ) -> None:
    url = "google"
    def monkey_valid_google_url(url):
        return result_valid_url

    def monkey_has_internet_connection():
        return result_has_internet

    monkeypatch.setattr(main, "valid_google_url", monkey_valid_google_url)
    monkeypatch.setattr(main, "has_internet_connection", monkey_has_internet_connection)
    assert main.can_access_google_page(url) == result_can_access