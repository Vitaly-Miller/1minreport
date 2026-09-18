"""
Pages fixtures
"""
import pytest
from playwright.sync_api import Page

from pages.home.home_page import HomePage
from pages.login.login_page import LoginPage

#=======================================================================================================================
#------------------------------------------------- Page (Guest Pages) --------------------------------------------------
@pytest.fixture
def home_page(page_guest: Page) -> HomePage:
    """
    Фикстура инициализации HomePage()

    :param page_guest: Фикстура guest_page (NO Storage State)
    :return: HomePage(page=guest_page)
    """
    return HomePage(page_guest)

@pytest.fixture
def login_page(page_guest: Page) -> LoginPage:
    """
    Фикстура инициализации LoginPage()

    :param page_guest: Фикстура guest_page (NO Storage State)
    :return: LoginPage(page=guest_page)
    """
    return LoginPage(page_guest)
#---------------------------------------------- Page (+ Storage State 📦) ----------------------------------------------


#=======================================================================================================================
