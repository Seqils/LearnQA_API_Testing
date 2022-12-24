import requests
import pytest

user_agents = [
    {'user_agent': 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 '
                   '(KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
     'expected_values': {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}},

    {'user_agent': 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 '
                   '(KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
     'expected_values': {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}},

    {'user_agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
     'expected_values': {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}},

    {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
     'expected_values': {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}},

    {'user_agent': 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 '
                   '(KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
     'expected_values': {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}}
]


@pytest.mark.parametrize('condition', user_agents)
def test_user_agent(condition):
    user_agent = condition['user_agent']
    headers = {'User-Agent': user_agent}
    expected_values = condition['expected_values']
    exp_platform = expected_values['platform']
    exp_browser = expected_values['browser']
    exp_device = expected_values['device']
    url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
    response = requests.get(url, headers=headers)
    response_json = response.json()
    platform = response_json['platform']
    browser = response_json['browser']
    device = response_json['device']

    assert platform == exp_platform, f"Wrong platform. Want [{exp_platform}], have [{platform}]"
    assert browser == exp_browser, f"Wrong browser. Want [{exp_browser}], have [{browser}]"
    assert device == exp_device, f"Wrong device. Want [{exp_device}], have [{device}]"


# FAILED test_user_agent.py::test_user_agent[condition1] - AssertionError: Wrong browser. Want [Chrome], have [No]
# FAILED test_user_agent.py::test_user_agent[condition2] - AssertionError: Wrong platform. Want [Googlebot], have [Unknown]
# FAILED test_user_agent.py::test_user_agent[condition4] - AssertionError: Wrong device. Want [iPhone], have [Unknown]
