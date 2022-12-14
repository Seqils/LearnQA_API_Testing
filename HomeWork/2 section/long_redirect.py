import requests

link_link = "https://playground.learnqa.ru/api/long_redirect"


def long_response(link):
    response = requests.get(link)
    history = response.history
    count = len(history)
    status = history[0].status_code
    last_redirection_url = history[-1].url
    response_url = response.url
    print(f"Количество редиректорв с кодом {status}: {count} \nПоследний редирект-URL: {last_redirection_url}"
          f"\nПоследний URL в запросе: {response_url}")


long_response(link_link)
