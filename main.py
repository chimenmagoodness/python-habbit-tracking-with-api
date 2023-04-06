from datetime import datetime

import requests

pexela_end_point = "https://pixe.la/v1/users"
TOKEN ="Switnex60887102'"
USERNAME = "switnex"
GRAPH_ID = "switnex1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pexela_end_point, json=user_params)
# print(response.text)

graph_endpoint = f"{pexela_end_point}/{USERNAME}/graphs"


graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "min ",
    "type": "int",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
new_day = today.strftime("%Y%m%d")
graph_update_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

graph_pixel_endpoint = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How Much time did you spend?: ")
}

response = requests.post(url=graph_update_endpoint, json=graph_pixel_endpoint, headers=headers)
print(response.text)

put_request_url = f"{pexela_end_point}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
graph_pixel_update = {
    "quantity": "20"
}
# response = requests.put(url=put_request_url, json=graph_pixel_update, headers=headers)
# print(response.text)

delete_pixel = f"{pexela_end_point}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_pixel, headers=headers)
# print(response.text)





