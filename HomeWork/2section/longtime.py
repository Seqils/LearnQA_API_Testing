import json
import requests
import time

link = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(link)
response_json = json.loads(response.text)
token = response_json["token"]
wait_time = response_json["seconds"] + 2
wrong_token = token + "G"
print(f"Задача создана, её токен: {token}")
good_params = {"token": f"{token}"}
wrong_params = {"token": f"{wrong_token}"}

print('Отправляем запрос с правильным токеном')
# response = requests.get(link, wrong_params)
response_ok = requests.get(link, good_params)
response_ok_json = json.loads(response_ok.text)
if response_ok_json["status"] == "Job is NOT ready":
    print(f"Пока всё хорошо, задача ещё не выполнена. Сообщение: {response_ok_json['status']}")
else:
    print("Что-то пошло не так")

time.sleep(wait_time)

response_result = requests.get(link, good_params)
response_json = json.loads(response_result.text)
if response_json["result"] != "" and response_json["status"] == "Job is ready":
    print(f'Всё отлично, результат: {response_json["result"]}')
else:
    print("Что-то пошло не так")
