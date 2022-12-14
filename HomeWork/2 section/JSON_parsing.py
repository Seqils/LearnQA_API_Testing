import json

string_json_text = '{"messages": [{"message": "This is the first message", "timestamp": "2021-06-04 16:40:53"},' \
            '{"message": "And this is a second message", "timestamp": "2021-06-04 16:41:01"}]}'


def json_parsing_var1(string):
    json_obj = json.loads(string)
    print(json_obj["messages"][1]["message"])


def json_parsing_var2(string):
    key = "messages"
    key_second = "message"
    json_obj = json.loads(string)
    messages = json_obj[key]
    message = messages[1]
    desired_message = message[key_second]
    print(desired_message)


json_parsing_var1(string_json_text)
json_parsing_var2(string_json_text)
