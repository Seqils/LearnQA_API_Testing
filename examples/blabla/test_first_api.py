import requests
import pytest


class TestFirstApi:
    names = [
        "Nikita",
        "Katya",
        ""
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name": name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong responce code"

        repsonse_dict = response.json()
        assert "answer" in repsonse_dict, "There is no 'answer' key"

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"
        actual_response_text = repsonse_dict["answer"]
        assert expected_response_text == actual_response_text, f"Wrong response. Want {expected_response_text}, " \
                                                               f"have {actual_response_text}"
