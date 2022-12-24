import requests


def first_get(link):
    payload = {"name": "Nikita"}
    response = requests.get(link, params=payload)
    return response.text

print(first_get("https://playground.learnqa.ru/api/hello"))