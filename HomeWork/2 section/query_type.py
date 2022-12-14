import requests

get_params = {"method": "GET"}
post_params = {"method": "POST"}
put_params = {"method": "PUT"}
delete_params = {"method": "DELETE"}
wrong_params = {"method": "HEAD"}
params = [get_params, post_params, put_params, delete_params, wrong_params]
link = "https://playground.learnqa.ru/ajax/api/compare_query_type"

get_response = requests.get(link)
print(f"Без параметра с указанным методом получаем сообщение: {get_response.text}")
post_response = requests.post(link, data=wrong_params)
print(f"Запрос с параметрами с неверным методом HEAD: {post_response.text}")
put_response = requests.put(link, data=put_params)
print(f"Запрос с верным методом в параметрах: {put_response.text}")

print(f"Проверяем запрос GET")
for i in range(len(params)):
    response = requests.get(link, params=params[i])
    print(f"Проверяем метод {params[i]['method']}, в ответ получаем сообщение: {response.text}")

print(f"Проверяем запрос POST")
for i in range(len(params)):
    response = requests.post(link, data=params[i])
    print(f"Проверяем метод {params[i]['method']}, в ответ получаем сообщение: {response.text}")

print(f"Проверяем запрос PUT")
for i in range(len(params)):
    response = requests.put(link, data=params[i])
    print(f"Проверяем метод {params[i]['method']}, в ответ получаем сообщение: {response.text}")

print(f"Проверяем запрос DELETE")
for i in range(len(params)):
    response = requests.delete(link, data=params[i])
    print(f"Проверяем метод {params[i]['method']}, в ответ получаем сообщение: {response.text}")


# Баг в запросе DELETE. При отправке параметров с методом GET получаем сообщение об успешно выполненном запросе
