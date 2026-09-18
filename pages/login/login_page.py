"""
Login page
https://www.1minreport.com/login
"""

import allure

from components.login.footer import LoginPageFooterComponent
from components.login.form import LoginFormComponent
from components.login.header import LoginPageHeaderComponent
from pages.base_page import BasePage
from playwright.sync_api import Page
from config import Endpoint

#=======================================================================================================================
class LoginPage(BasePage):
    """
    - Header (component)
    - Form (component)
    - Footer (component)
    """
    URL = Endpoint.LOGIN
    PATH = 'Login page'

    def __init__(self, page: Page):
        super().__init__(page)

        # ⿳ COMPONENTS
        self.header = LoginPageHeaderComponent(page)
        self.form = LoginFormComponent(page)
        self.footer = LoginPageFooterComponent(page)



    # -------------------------------------------------- ✔️EXPECTATIONS ------------------------------------------------
    # [Page]
    # ──────────────────────────────────────┐
    @allure.step('✔ Check [Login page] UI')
    def check(self):
        """
        ✔ Check [Login page] UI

        - ✔ Header (component)
        - ✔ Form (component)
        - ✔ Footer (component)
        """
        self.header.check()
        self.form.check()
        self.footer.check()
    # ──────────────────────────────────────┘


#=======================================================================================================================
