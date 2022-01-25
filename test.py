import requests
import json
def fly_book(message):
    url = 'https://open.feishu.cn/open-apis/bot/v2/hook/ce0dc2c7-1b5e-479c-a9f0-b8c2a53ee421'
    payload_message = {
    "msg_type": "text",
    "content": {
        "text": message
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }

    requests.request("POST", url, headers=headers, data=json.dumps(payload_message))
fly_book('nihao')