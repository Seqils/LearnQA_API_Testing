import requests

link = "https://playground.learnqa.ru/api/get_301"


response = requests.post(link, allow_redirects=True)
first_response = response.history[0]
second_response = response

print(first_response.url)
print(first_response.status_code)
print(second_response.url)
print(response.status_code)


