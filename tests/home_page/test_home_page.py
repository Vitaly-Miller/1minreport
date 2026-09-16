"""
Test Home page
"""

import allure
from allure_commons.types import Severity
from pages.home.home_page import HomePage
from tools.allure.annotations import Epic, Feature, Story, Tag

#=======================================================================================================================
@allure.severity(Severity.NORMAL)
@allure.tag(Tag.HOME_PAGE, Tag.EXPLORATION, Tag.UI)
@allure.epic(Epic.HOME_PAGE)
@allure.feature(Feature.UI)
@allure.story(Story.EXPLORATION)
class TestHomePage:
    @allure.title('✔ Check [Header]')
    def test_header(self, home_page: HomePage):
        # ⿹ Open page
        home_page.open(home_page.URL)
        # ✔️EXPECTATIONS
        home_page.check()             # Test suite (33 sub-steps)

#=======================================================================================================================
