"""
Login page footer (component)
"""
import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.text import Text


#=======================================================================================================================
class LoginPageFooterComponent(BaseComponent):
    """
    - Slogan
    """
    PATH = 'Login page > Footer'

    # --------------------------------------------------- ㉧ LOCATORS ---------------------------------------------------
    def slogan_locator(self) -> Locator:
        return self.page.locator('div.mt-8')


    # --------------------------------------------------- ◈ ELEMENTS ---------------------------------------------------
    def slogan(self) -> Text:
        return Text(self.slogan_locator(), self.PATH, 'Slogan')


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Footer]
    # ──────────────────────────────────┐
    @allure.step('✔ Check [Footer]')
    def check(self):
        """
        ✔ Check [Footer]

        - ✔ Slogan
        """
        self.check_slogan()
    # ──────────────────────────────────┘

    # [Slogan]
    @allure.step('✔ Check [Slogan]')
    def check_slogan(self):
        """
        ✔ Check [Slogan]

        - ✔ Slogan - visible
        - ✔ Slogan - text
        """
        self.slogan().check_visible()
        self.slogan().check_text('Built for the people who make a difference.')


#=======================================================================================================================
