import requests

link = "https://playground.learnqa.ru/api/check_type"
payload = {"par1": "val1"}
data = {"par10000": "val10000"}
response = requests.post(link, params=payload)
print(response.text)
