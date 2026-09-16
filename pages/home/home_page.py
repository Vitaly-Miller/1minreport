"""
Home page
https://www.1minreport.com/
"""

import allure
from components.navigation.header.header_component import HeaderComponent
from pages.base_page import BasePage
from playwright.sync_api import Locator, Page
from config import Endpoint

#=======================================================================================================================
class HomePage(BasePage):                      # Дочерний класс (наследует класс BasePage)
    """
    [Home page]

    - Header (component)
    - Footer (component)
    - ...

    """
    URL = Endpoint.HOME
    PATH = 'Home page'                         # for logging

    def __init__(self, page: Page):            # Конструктор класса, принимающий Page
        super().__init__(page)                 # Передаёт page в конструктор BasePage

        # ⿳ COMPONENTS
        self.header = HeaderComponent(page)

    # -------------------------------------------------- ✔️EXPECTATIONS ------------------------------------------------
    # [Page]
    # ──────────────────────────────────────┐
    @allure.step('✔ Check [Home page]')
    def check(self):
        """
        ✔ Check [Home page]

        - ✔ Header (component)
        - ✔ ...
        - ✔ ...
        - ✔ ...
        """
        self.header.check()
    # ──────────────────────────────────────┘


#=======================================================================================================================
