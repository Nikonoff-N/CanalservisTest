#!/usr/bin/env python3


# import requests
# token = "2034272816:AAERLHI8XdQmSDTAgXBEvslDYBxOof0tpwg"
# channel_id = "@CanalTest"
# requests.post('https://api.telegram.org/bot{token}/sendMessage?chat_id=<yourchatid>&text=Hello World!')

import requests

def send_telegram(text: str):
    token = "2034272816:AAERLHI8XdQmSDTAgXBEvslDYBxOof0tpwg"
    url = "https://api.telegram.org/bot"
    channel_id = "-1001524461147"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

if __name__ == '__main__':
  send_telegram("hello world!")