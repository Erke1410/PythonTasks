import requests

from Api.data import LocalData


def api_create_request(name, number):
    payload = {
        "title": f"{name}",
        "body": f"{number}",
    }
    request = requests.put("https://jsonplaceholder.typicode.com/posts/1", data=payload)
    request_id = request.json().get("id")
    status = request.status_code
    print(status)
    print(request.json())
    print(request_id)
    assert status == 200, "Request is not created"
    return request_id


def api_get_request(numbers):
    request = requests.get(LocalData.jsonPlaceHolder_post + f"/{numbers}")
    print(request.json())
    print(request.status_code)

    assert request.status_code == 200, "Request cannot be found"


def delete_request(nmbr):
    request = requests.delete(LocalData.jsonPlaceHolder_post + f"/{nmbr}")
    print(request.status_code)

    assert request.status_code == 200, "Request is not deleted!"