from urllib import response
import requests
import json
import appkey

# start_date = '2021-01-01 00:00:00'
# end_date = '2021-12-31 00:00:00'


# headers={'Authorization':appkey}
# #AppURL = f'https://api.nexon.co.kr/kart/v1.0/users/nickname/{nickname}'
# matchURL = f'https://api.nexon.co.kr/kart/v1.0/matches/all?start_date={start_date}&end_date={end_date}'

# ##req=requests.get(AppURL,headers=headers)
# req=requests.get(matchURL,headers=headers)

# if req.status_code == 200:
#     print("정상출력")
#     print(req.json())
# else:
#     print(req.status_code)

slack_token = appkey.slack_token

def post_message (token, channel, text):

    response = requests.post("https://slack.com/api/chat.postMessage",
    headers = {"Authorization" : "Bearer " + token},
    data = {"channel" : channel , "text" : text}
    )

    print(response)

post_message(slack_token,'#portfolio','success message post')