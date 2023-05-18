import requests
import json
from bson import ObjectId



# def post_request():
#     # set the URL of the API endpoint
#     url = "http://127.0.0.1:5000/books"
#
#     # set the JSON request payload
#     payload = {
#         "bot_id": 10
#     }
#
#     # convert the payload to a JSON string
#     json_payload = json.dumps(payload)
#
#     # set the headers of the request
#     headers = {
#         "Content-Type": "application/json"
#     }
#
#     # send the POST request with the JSON payload
#     response = requests.post(url, data=json_payload, headers=headers)
#
#     # get the response status code and content
#     if not response.ok:
#         return False
#     else:
#         return True

# def delete_request():
#     # URL of the API endpoint
#     url = 'http://127.0.0.1:5000/books/173ed8821adb420881e6c7691ee94fea'
#
#     # Data to be sent in the PUT request
#     put_data = {'title': 'On the Road', 'author': 'Jack Kerouac', 'read': False}
#
#     # Make the PUT request
#     response = requests.put(url, json=put_data)
#
#     # Print the response
#     print(response.json())
#
#     # Data to be sent in the DELETE request
#     delete_data = {}
#
#     # Make the DELETE request
#     response = requests.delete(url, json=delete_data)
#
#     # Print the response
#     print(response.json())

def db_request():
    url = "http://127.0.0.1:5000/data"

    # set the JSON req payload
    payload = {
        "FirstName": "Joash",
        "LastName": "Law",
        "DOB": 11022003,
        "Contact": 91500846,
        "Email": "joashlaw75@gmail.com",
        "PW": "xtyxcykthgfcgvk"
    }

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

# send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}") # f"Response Content: {content}")

def update_request():
    url = "http://127.0.0.1:5000/update-data"

    # set the JSON req payload
    payload = {
        "document_id": str(ObjectId("6465c6f848faf7e66a5bd750")),
        "FirstName": "Joash",
        "LastName": "Law",
        "DOB": "11-02-2003",
        "Contact": 91500846,
        "Email": "joashlaw75@gmail.com",
        "PW": "xtyxcykthgfcgvk"
    }

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

# send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}") # f"Response Content: {content}")

def delete_request():
    url = "http://127.0.0.1:5000/delete-data"

    # set the JSON req payload
    payload = {
        "document_id": str(ObjectId("6465c6f848faf7e66a5bd750")),
    }

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

# send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}") # f"Response Content: {content}")

def getcup_request():  # first scan at kiosk

    payload = {
        "document_id": str(ObjectId("6465d811b732336bb5bcb3b9"))
    }

    # set the JSON req payload
    url = f'http://127.0.0.1:5000/{payload["document_id"]}/cups'

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.get(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}")

def updatecup_request():  # when they purchase a cup

    # set the JSON req payload
    payload = {
        "document_id": str(ObjectId("6465d811b732336bb5bcb3b9"))
    }

    url = f'http://127.0.0.1:5000/{payload["document_id"]}/cups'

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}")

# def post_request():
#     # set the URL of the API endpoint
#     url = "http://127.0.0.1:5000/db/insertrun"
#
#     # set the JSON request payload
#     payload = {
#         "bot_id": 10
#     }
#
#     # convert the payload to a JSON string
#     json_payload = json.dumps(payload)
#
#     # set the headers of the request
#     headers = {
#         "Content-Type": "application/json"
#     }
#
#     # send the POST request with the JSON payload
#     response = requests.post(url, data=json_payload, headers=headers)
#
#     # get the response status code and content
#     if not response.ok:
#         return InsertBotRunResponse(status=ResponseStatus.FAILED, data=InsertBotRunFail(json.loads(response.text)))
#     return InsertBotRunResponse(status=ResponseStatus.SUCCESS, data=InsertBotRunSuccess(json.loads(response.text)))
#
#
# def update_request(botrun_id):
#     # set the URL of the API endpoint
#     url = "http://127.0.0.1:5000/db/updaterun"
#
#     # set the JSON request payload
#     payload = {
#         "botrun_id": botrun_id,
#         "status": 1,
#         "remarks": ''
#     }
#
#     # convert the payload to a JSON string
#     json_payload = json.dumps(payload)
#
#     # set the headers of the request
#     headers = {
#         "Content-Type": "application/json"
#     }
#
#     # send the POST request with the JSON payload
#     response = requests.post(url, data=json_payload, headers=headers)
#
#     # get the response status code and content
#     status_code = response.status_code
#     content = response.content
#
#     # print the response status code and content
#     print(f"Response Status Code: {status_code}")
#     print(f"Response Content: {content}")





if __name__ == '__main__':
    # print(post_request())

    # db_request()
    # update_request()
    # delete_request()
    # getcup_request()
    updatecup_request()

