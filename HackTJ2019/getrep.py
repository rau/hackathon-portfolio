# We'll use the `requests` module to make our HTTP Request
import requests

# We'll use the `json` module to format our response's data
import json

# Our Phone2Action API Key goes here
# Super important, we need this to show that we're authorized to make our request
x_api_key = ""  # Should not be empty
# See the README for info on how to get an API Key

# First, we define our base URL and our parameters
# Our parameters can be a Dictionary, since the `requests` module converts them
# Our headers can also be a Dictionary, `requests` converts these as well


def getTwitter(address):
    endpoint = (
        "https://fmrrixuk32.execute-api.us-east-1.amazonaws.com/hacktj/legislators"
    )
    parameters = {"level": "NATIONAL_LOWER", "address": address}
    headers = {"X-API-Key": x_api_key}

    # Now, we're able to fire the configured HTTP GET request
    response = requests.get(endpoint, params=parameters, headers=headers)

    # Next, we convert the response to a JSON with `json.loads()`
    representatives = json.loads(response.text)["officials"]

    # Finally, we pick out the data we want and print it to the console
    # Use Postman to figure out what format your data is in and access it accordingly
    # A sample JSON is also available at https://github.com/phone2action/hacktj-examples#legislators-api
    for representative in representatives:
        socials = representative["socials"]
        for social in socials:
            if social["identifier_type"] == "TWITTER":
                return social["identifier_value"]

        return ""


def getName(address):
    endpoint = (
        "https://fmrrixuk32.execute-api.us-east-1.amazonaws.com/hacktj/legislators"
    )
    parameters = {"level": "NATIONAL_LOWER", "address": address}
    headers = {"X-API-Key": x_api_key}

    # Now, we're able to fire the configured HTTP GET request
    response = requests.get(endpoint, params=parameters, headers=headers)

    # Next, we convert the response to a JSON with `json.loads()`
    representatives = json.loads(response.text)["officials"]

    # Finally, we pick out the data we want and print it to the console
    # Use Postman to figure out what format your data is in and access it accordingly
    # A sample JSON is also available at https://github.com/phone2action/hacktj-examples#legislators-api
    for representative in representatives:
        first_name = representative["first_name"]
        last_name = representative["last_name"]
        return first_name + " " + last_name
