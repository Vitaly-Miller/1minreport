"""
Pages fixtures
"""
import pytest
from playwright.sync_api import Page

from pages.home.home_page import HomePage

#=======================================================================================================================
#------------------------------------------- Chromium Pages (Guest Pages) ----------------------------------------------
@pytest.fixture
def home_page(page_guest: Page) -> HomePage:
    """
    Фикстура инициализации HomePage()

    :param page_guest: Фикстура guest_page (NO Storage State)
    :return: HomePage(page=guest_page)
    """
    return HomePage(page_guest)

#---------------------------------------- Chromium Pages (+ Storage State 📦) ------------------------------------------


#=======================================================================================================================
