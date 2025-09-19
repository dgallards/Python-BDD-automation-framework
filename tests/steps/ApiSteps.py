from behave import given, when, then
import requests
import json
from jsonschema import validate, ValidationError
from settings.logging import log

@given('The API uri is set to "{uri}"')
def step_given_api_uri(context, uri_json, item_tag):  
    with open(uri_json, 'r') as file:
        data = json.load(file)
    context.api_url = data[item_tag]
    log(context, f"API URL set to {context.api_url}")

@given('the API endpoint is set to "{url}"')
def step_given_api_endpoint(context, url):
    context.api_url = url
    log(context, f"Endpoint set to: {url}")

@when('a GET request is sent to the API')
def step_when_get_request(context):
    context.response = requests.get(context.api_url)
    log(context, f"GET request to {context.api_url}, status code: {context.response.status_code}")
    log(context, f"Response body:\n{context.response.text}")

@when('prepare the body request with the data in "{file_name}"')
def step_when_prepare_body_request(context, file_name):
    with open(file_name, 'r') as file:
        context.request_data = file.read()
    log(context, f"Prepared request body from file: {file_name}")
    log(context, f"Request body:\n{context.request_data}")

@when('a POST request is sent to the API with the body')
def step_when_post_request(context):
    context.response = requests.post(context.api_url, data=context.request_data)
    log(context, f"POST request to {context.api_url}, status code: {context.response.status_code}")
    log(context, f"Response body:\n{context.response.text}")

@then('the response status code should be {status_code:d}')
def step_then_status_code(context, status_code):
    actual = context.response.status_code
    log(context, f"Asserting response status: expected {status_code}, got {actual}")
    assert actual == status_code, f"Expected {status_code}, got {actual}"

@then('the response should contain "{key}" with value "{value}"')
def step_then_response_contains(context, key, value):
    response_json = context.response.json()
    log(context, f"Asserting response key '{key}' has value '{value}'")
    assert key in response_json, f"Key '{key}' not found in response"
    assert str(response_json[key]) == value, f"Expected {value}, got {response_json[key]}"

@then('the response should match the schema in "{schema_file}"')
def step_then_match_schema(context, schema_file):
    with open(schema_file, 'r') as file:
        schema = json.load(file)
    response_json = context.response.json()
    try:
        validate(instance=response_json, schema=schema)
        log(context, f"Response matches schema from {schema_file}")
    except ValidationError as e:
        log(context, f"Schema validation failed: {e.message}")
        raise AssertionError(f"Response does not match schema: {e.message}")

@then('clear the API response data')
def step_then_clear_response(context):
    context.response = None
    context.api_url = None
    log(context, "API response and URL cleared.")
