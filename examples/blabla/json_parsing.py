import requests
import json


def first_json(link):
    payload = {"name": "Nikita"}
    response = requests.get(link, params=payload)
    print(response.text)
    string = response.text
    json_obj = json.loads(string)
    # return response
    key = "answer"

    if key in json_obj:
        return json_obj[key]
    else:
        return f"No {key} key in JSON"


print(first_json("https://playground.learnqa.ru/api/hello"))
