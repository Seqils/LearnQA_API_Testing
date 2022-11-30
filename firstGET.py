import requests


def first_get(link):
    response = requests.get(link)
    return response.text

print(first_get("https://playground.learnqa.ru/api/get_text"))