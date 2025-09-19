
    @apis
Feature: Basic API testing
    This feature performs GET and POST requests using JSONPlaceholder and validates responses.

  Scenario Outline: GET a single post by ID
    Given the API endpoint is set to "https://jsonplaceholder.typicode.com/posts/<id>"
    When a GET request is sent to the API
    Then the response status code should be 200
    Then the response should match the schema in "tests/helpers/schemas/get_schema.json"
    And the response should contain "id" with value "<id>"
    Then clear the API response data
    Examples:
      | id |
      | 1  |
      | 2  |
      | 3  |
      

    Scenario: GET all posts
     Given the API endpoint is set to "https://jsonplaceholder.typicode.com/posts"
     When a GET request is sent to the API
     Then the response status code should be 200
     Then the response should match the schema in "tests/helpers/schemas/get_list_schema.json"

  Scenario: Create a new post
    Given the API endpoint is set to "https://jsonplaceholder.typicode.com/posts"
    When prepare the body request with the data in "tests/helpers/data/new_post.json" 
    And a POST request is sent to the API with the body
    Then the response status code should be 201
    Then the response should match the schema in "tests/helpers/schemas/post_schema.json"

  Scenario: Cleanup
    Then clear the API response data
