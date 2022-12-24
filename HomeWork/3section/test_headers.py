import requests


def test_headers():
    name = 'success'
    value = '!'
    url = "https://playground.learnqa.ru/api/homework_header"
    response = requests.get(url)
    json_dict = response.json()

    assert name in json_dict, f"There is no '{name}' key in json"
    assert json_dict[name] == value, f"Wrong value for '{name}' key. Have '{json_dict[name]}', want '{value}'"
