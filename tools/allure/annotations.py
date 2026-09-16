"""
Allure Annotations + Enum
"""

from enum import StrEnum

#=======================================================================================================================
# ⚠️Python 3.11- ⮕ class ...(str, Enum):
# ⚠️Python 3.11+ ⮕ class ...(StrEnum):

#----------------------------------------------------- Allure Tags -----------------------------------------------------
# @allure.tag(Tag.<...>)
class Tag(StrEnum):
    HOME_PAGE = 'HOME PAGE'
    REG_PAGE = 'REGISTRATION PAGE'
    LOGIN_PAGE = 'LOGIN PAGE'
    #------------------------
    REGRESSION = 'REGRESSION'
    SMOKE = 'SMOKE'
    EXPLORATION = 'EXPLORATION'
    NEGATIVE = 'NEGATIVE'
    VALIDATE = 'VALIDATE'
    #-------------------
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    NAVIGATE = 'NAVIGATE'
    #--------------------------
    PARAMETRIZE = 'PARAMETRIZE'
    UI = 'UI'


#---------------------------------------------- Allure Behaviors / Suites ----------------------------------------------
# @allure.epic() / @allure.parent_suite()
class Epic(StrEnum):
    HOME_PAGE = 'Home page'
    LOGIN_PAGE = 'Login page'
    REG_PAGE = 'Registration page'


# @allure.feature() / @allure.suite()
class Feature(StrEnum):
    LOGIN = 'Login feature'
    REGISTRATION = 'Registration feature'
    UI = 'UI'


# @allure.story() / @allure.sub_suite()
class Story(StrEnum):
    # Positive scenario
    REGISTRATION = 'Registration'
    LOGIN = 'Login'
    EXPLORATION = 'Exploration'

    CREATE = 'Create'
    UPDATE = 'Update'
    DELETE = 'Delete'
    NAVIGATE = 'Navigate'

    # Negative scenario
    REGISTRATION_NEGATIVE = 'Registration (negative)'
    LOGIN_NEGATIVE = 'Login (negative)'
    CREATE_NEGATIVE = 'Create (negative)'
    UPDATE_NEGATIVE = 'Update (negative)'
    DELETE_NEGATIVE = 'Delete (negative)'
    NAVIGATE_NEGATIVE = 'Navigate (negative)'



#=======================================================================================================================
