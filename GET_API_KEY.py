import requests

get_headers = {
    "email": "abc1234@mail.ru",
    "password": "abc1234"
}

get_params = get_headers

api_key_link = "https://petfriends1.herokuapp.com/api/key"

response = requests.get(api_key_link,
                        params=get_params,
                        headers=get_headers
                        )
if response.status_code == 200:
    print("OK")

if response.ok:
    print("OK")

print(response.text)