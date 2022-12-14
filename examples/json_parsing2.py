from json.decoder import JSONDecodeError
import requests

link = "https://playground.learnqa.ru/api/hello"
key = "answer"
wrong_link = "https://playground.learnqa.ru/api/get_text"


def json_parsing(link, key):
    payload = {"name": "Nikita"}
    response = requests.get(link, params=payload)
    parsed_response_text = response.json()
    return parsed_response_text[key]


try:
    print(json_parsing(link, key))
except JSONDecodeError:
    print("Response is not a JSON format")

try:
    print(json_parsing(wrong_link, key))
except JSONDecodeError:
    print("Response is not a JSON format")