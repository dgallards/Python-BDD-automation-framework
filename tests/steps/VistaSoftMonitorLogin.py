from behave import *

import CommonStep
import WebElements


@then('I verify that the "{error_message}" should be displayed')
def i_verify_that_the_error_message_should_be_displayed(context, error_message):
    element_error_message = CommonStep.presence_element_located_find_by_id(context, WebElements.GET_LOGIN_ERROR_MESSAGE)

    if not element_error_message.is_displayed():
        raise AssertionError("Error message not display")
    if element_error_message.text != error_message:
        raise AssertionError(f"Wrong error message display: actual error message: {element_error_message.text},"
                             f" expected error message: {error_message}")


@then('I verify that I able to navigate to Dashboard at "{expected_url}"')
def i_validate_that_i_navigate_to_my_user_account(context, expected_url):
    element_dashboard_label = CommonStep.visibility_element_located_find_by_xpath(context,
                                                                                  WebElements.GET_DASHBOARD_LABEL)

    actual_url = context.driver.current_url

    if actual_url != expected_url:
        raise AssertionError(f"Did not navigate to expected url: {expected_url}, but navigate to: {actual_url}")
    if element_dashboard_label.text != 'Dashboard':
        raise AssertionError(f"Wrong page displayed: {element_dashboard_label.text}, "
                             f"expected page: Dashboard")
