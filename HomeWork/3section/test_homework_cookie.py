import requests

def test_homework_cookie():
    name = "HomeWork"
    value = "hw_value"
    url = "https://playground.learnqa.ru/api/homework_cookie"
    response = requests.get(url)
    cookies = dict(response.cookies)
    assert name in cookies, f"There is no '{name}' cookie, something went wrong"
    assert value in cookies[name], f"There is no '{value}' for '{name}' cookie, something went wrong"
