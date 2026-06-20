import pytest
from pages.social.notification_page import NotificationPage


@pytest.mark.social
class TestNotifications:
    def test_notification_appears(self, driver):
        page = NotificationPage(driver).open_notifications()
        page.trigger_notification()
        msg = page.get_notification_text()
        assert len(msg) > 0

    def test_notification_has_content(self, driver):
        page = NotificationPage(driver).open_notifications()
        page.trigger_notification()
        msg = page.get_notification_text()
        assert "Action" in msg or "unsuccesful" in msg or "successful" in msg


@pytest.mark.social
class TestInteractions:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = NotificationPage(driver).open_add_remove()

    def test_add_interaction(self, driver):
        self.page.add_element()
        assert self.page.get_delete_buttons_count() == 1

    def test_add_multiple_interactions(self, driver):
        for _ in range(5):
            self.page.add_element()
        assert self.page.get_delete_buttons_count() == 5

    def test_remove_interaction(self, driver):
        self.page.add_element()
        self.page.add_element()
        self.page.delete_element(0)
        assert self.page.get_delete_buttons_count() == 1

    def test_add_and_remove_all(self, driver):
        for _ in range(3):
            self.page.add_element()
        assert self.page.get_delete_buttons_count() == 3
        for _ in range(3):
            self.page.delete_element(0)
        assert self.page.get_delete_buttons_count() == 0


@pytest.mark.social
class TestTogglePreferences:
    def test_checkbox_initial_state(self, driver):
        page = NotificationPage(driver).open_checkboxes()
        assert not page.is_checkbox_checked(0)
        assert page.is_checkbox_checked(1)

    def test_toggle_checkbox_on(self, driver):
        page = NotificationPage(driver).open_checkboxes()
        page.toggle_checkbox(0)
        assert page.is_checkbox_checked(0)

    def test_toggle_checkbox_off(self, driver):
        page = NotificationPage(driver).open_checkboxes()
        page.toggle_checkbox(1)
        assert not page.is_checkbox_checked(1)

    def test_toggle_both(self, driver):
        page = NotificationPage(driver).open_checkboxes()
        page.toggle_checkbox(0)
        page.toggle_checkbox(1)
        assert page.is_checkbox_checked(0)
        assert not page.is_checkbox_checked(1)
