from Api.API_test1 import api_create_request, api_get_request, delete_request

num = api_create_request("Jovan", "1234567")
api_get_request(num)
delete_request(num)