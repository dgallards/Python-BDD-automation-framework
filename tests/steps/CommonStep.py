import WebElements
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from selenium import webdriver

TIMEOUT = 100


@given('I am on "{url}" - VS Monitor Homepage')
def i_am_on_vs_monitor_homepage(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@given('I enter "{username}" for username and "{password}" for password')
def i_enter_the_credential(context, username, password):
    element_username = presence_element_located_find_by_id(context, WebElements.GET_USERNAME_INPUT_AT_LOGIN_PAGE)
    element_username.send_keys(username)

    element_password = presence_element_located_find_by_id(context, WebElements.GET_PASSWORD_INPUT_AT_LOGIN_PAGE)
    element_password.send_keys(password)


@when('I click on Login button in VS Monitor Homepage')
def i_click_on_login_button_in_vs_monitor_homepage(context):
    element = presence_element_located_find_by_xpath(context, WebElements.GET_LOGIN_BUTTON_AT_HOMEPAGE)
    element.click()


@when('I click on LOG-IN button on Log-in page')
def i_click_on_login_button_on_login_page(context):
    element_login_button = presence_element_located_find_by_xpath(context, WebElements.GET_LOGIN_BUTTON_AT_LOGIN_PAGE)
    element_login_button.submit()


@then("I validate that I navigate to Login page")
def i_able_to_validate_that_i_navigate_to_login_page(context):
    element_login_label = presence_element_located_find_by_xpath(context, WebElements.GET_LOGIN_LABEL_AT_LOGIN_PAGE)
    element_username = presence_element_located_find_by_id(context, WebElements.GET_USERNAME_INPUT_AT_LOGIN_PAGE)
    element_password = presence_element_located_find_by_id(context, WebElements.GET_PASSWORD_INPUT_AT_LOGIN_PAGE)
    element_login_button = presence_element_located_find_by_xpath(context, WebElements.GET_LOGIN_BUTTON_AT_LOGIN_PAGE)

    if (not element_login_label and not element_username.is_displayed()
            and not element_password.is_displayed() and not element_login_button.is_displayed()):
        get_element_in_login_page_is_displayed(element_login_label, element_password, element_username,
                                               element_login_button)
        raise AssertionError("Element not found")


def get_element_in_login_page_is_displayed(element_login_label, element_password, element_username,
                                           element_login_button):
    print("element_login_label : ", element_login_label.is_displayed())
    print("element_username : ", element_username.is_displayed())
    print("element_password : ", element_password.is_displayed())
    print("element_login_button : ", element_login_button.is_displayed())


def get_mobile_screen_size(context):
    return context.driver.get_window_size().get("width") < 1024


def presence_element_located_find_by_xpath(context, web_element):
    return WebDriverWait(context.driver, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, web_element)))

def presence_element_located_find_by_id(context, web_element):
    return WebDriverWait(context.driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, web_element)))

def visibility_element_located_find_by_xpath(context, web_element):
    return WebDriverWait(context.driver, TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, web_element)))

def visibility_element_located_find_by_id(context, web_element):
    # This function is specifically for By.ID. If GET_USER_FIRST_NAME becomes an XPath,
    # you'll need to use visibility_element_located_find_by_xpath
    return WebDriverWait(context.driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, web_element)))

# --- NEW / MODIFIED FUNCTION ---
def wait_for_element_and_get(context, by_locator, locator_value, wait_condition=EC.visibility_of_element_located):
    """
    Waits for an element based on a given locator and condition, then returns the element.
    :param context: The Behave context.
    :param by_locator: The By strategy (e.g., By.ID, By.XPATH, By.NAME).
    :param locator_value: The value of the locator (e.g., "firstName", "//div[@id='myDiv']").
    :param wait_condition: The expected condition to wait for (e.g., EC.visibility_of_element_located).
    :return: The WebElement once the condition is met.
    """
    return WebDriverWait(context.driver, TIMEOUT).until(wait_condition((by_locator, locator_value)))
