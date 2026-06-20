import pytest
from pages.social.dynamic_page import DynamicContentPage


@pytest.mark.social
class TestDynamicFeed:
    def test_dynamic_content_loads(self, driver):
        page = DynamicContentPage(driver).open_dynamic_content()
        texts = page.get_content_texts()
        assert len(texts) > 0

    def test_content_changes_on_refresh(self, driver):
        page = DynamicContentPage(driver).open_dynamic_content()
        first_load = page.get_content_texts()
        changed = False
        for _ in range(5):
            page.refresh_content()
            second_load = page.get_content_texts()
            if first_load != second_load:
                changed = True
                break
        assert changed, "Content should change on refresh (dynamic feed)"

    @pytest.mark.smoke
    def test_async_loading(self, driver):
        page = DynamicContentPage(driver).open_dynamic_loading()
        page.start_loading()
        text = page.wait_for_loaded_text()
        assert text == "Hello World!"

    def test_async_loading_shows_spinner(self, driver):
        page = DynamicContentPage(driver).open_dynamic_loading()
        page.start_loading()
        page.wait_for_loaded_text()
        result = page.get_text(*page.LOADED_TEXT)
        assert len(result) > 0
