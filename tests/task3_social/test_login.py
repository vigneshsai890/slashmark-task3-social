import pytest
from pages.social.login_page import HerokuLoginPage


@pytest.mark.social
class TestSocialLogin:
    def test_valid_login(self, driver):
        page = HerokuLoginPage(driver).open()
        page.login("tomsmith", "SuperSecretPassword!")
        assert page.is_logged_in()
        assert "secure" in page.get_flash_message().lower() or "logged" in page.get_flash_message().lower()

    def test_invalid_username(self, driver):
        page = HerokuLoginPage(driver).open()
        page.login("wronguser", "SuperSecretPassword!")
        msg = page.get_flash_message()
        assert "invalid" in msg.lower() or "error" in msg.lower()

    def test_invalid_password(self, driver):
        page = HerokuLoginPage(driver).open()
        page.login("tomsmith", "wrongpassword")
        msg = page.get_flash_message()
        assert "invalid" in msg.lower() or "error" in msg.lower()

    @pytest.mark.parametrize("username,password", [
        ("", "SuperSecretPassword!"),
        ("tomsmith", ""),
        ("", ""),
    ])
    def test_empty_credentials(self, driver, username, password):
        page = HerokuLoginPage(driver).open()
        page.login(username, password)
        msg = page.get_flash_message()
        assert "invalid" in msg.lower() or "error" in msg.lower()

    def test_login_logout_cycle(self, driver):
        page = HerokuLoginPage(driver).open()
        page.login("tomsmith", "SuperSecretPassword!")
        assert page.is_logged_in()
        page.logout()
        msg = page.get_flash_message()
        assert "logged out" in msg.lower()

    def test_multiple_login_attempts(self, driver):
        page = HerokuLoginPage(driver).open()
        page.login("wrong", "wrong")
        page.login("tomsmith", "SuperSecretPassword!")
        assert page.is_logged_in()
