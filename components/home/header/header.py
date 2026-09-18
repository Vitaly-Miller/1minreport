"""
Home page header
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.home.header.header_buttons import HeaderButtonsComponent
from components.home.header.header_logo import HeaderLogoComponent
from components.home.header.header_nav_links import HeaderNavLinksComponent

#=======================================================================================================================
class HeaderComponent(BaseComponent):
    """
    Header component

    - Logo
    - Navigation links
    - Authentication buttons
    """
    def __init__(self, page: Page):
        super().__init__(page)

        # ⿳ COMPONENTS
        self.logo = HeaderLogoComponent(page)
        self.nav_links = HeaderNavLinksComponent(page)
        self.buttons = HeaderButtonsComponent(page)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Header]
    # ───────────────────────────────┐
    @allure.step('✔ Check [Header]')
    def check(self):
        """
        ✔ Check [Header]

        - ✔ Logo
        - ✔ Navigation links (anchors)
        - ✔ Buttons
        """
        self.logo.check()
        self.nav_links.check()
        self.buttons.check()
    # ───────────────────────────────┘

#=======================================================================================================================
