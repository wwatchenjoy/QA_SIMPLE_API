import requests

# "key": "003c6904c7f44a085a12f9bf146415bb3d72270254cfd4dc8e0bd1e2"


# POST PET SIMPLE
post_headers = {
    "auth_key": "003c6904c7f44a085a12f9bf146415bb3d72270254cfd4dc8e0bd1e2",
    "name": "Bob",
    "animal_type": "German Shepherd",
    "age": '2'
}

post_params = post_headers
create_pet_simple_POST_link = "https://petfriends1.herokuapp.com/api/create_pet_simple"


def post_simple_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers
                             )

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(post_simple_pet(create_pet_simple_POST_link, post_params, post_headers))
