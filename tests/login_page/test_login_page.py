"""
Test Login page
"""

import allure
from allure_commons.types import Severity
from pages.login.login_page import LoginPage
from tools.allure.annotations import Epic, Feature, Story, Tag

#=======================================================================================================================
@allure.severity(Severity.NORMAL)
@allure.tag(Tag.HOME_PAGE, Tag.EXPLORATION, Tag.UI)
@allure.epic(Epic.LOGIN_PAGE)
@allure.feature(Feature.UI)
@allure.story(Story.EXPLORATION)
class TestLoginPage:
    @allure.title('✔ Check [Login page header] UI')
    def test_login_page_ui(self, login_page: LoginPage):
        # ⿹ Open page
        login_page.open(login_page.URL)
        # ✔️EXPECTATIONS
        login_page.check()             # Test suite (55 sub-steps)


#=======================================================================================================================
