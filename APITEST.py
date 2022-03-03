from urllib import response
import requests
import json
import appkey

start_date = '2021-01-01 00:00:00'
end_date = '2021-12-31 00:00:00'

slack_token = appkey.slack_token

def post_message (token, channel, text):

    response = requests.post("https://slack.com/api/chat.postMessage",
    headers = {"Authorization" : "Bearer " + token},
    data = {"channel" : channel , "text" : text}
    )

    print(response)

nexon_appkey = appkey.appkey

# request 시에 필수로 headers 사용
headers={'Authorization':nexon_appkey}

#AppURL = f'https://api.nexon.co.kr/kart/v1.0/users/nickname/{nickname}'
matchURL = f'https://api.nexon.co.kr/kart/v1.0/matches/all?start_date={start_date}&end_date={end_date}'

##req=requests.get(AppURL,headers=headers)
req=requests.get(matchURL,headers=headers)

if req.status_code == 200:
    data = req.json()
    match_id = data['matches'][0]['matches'][0]
    target_matchURL = f'https://api.nexon.co.kr/kart/v1.0/matches/{match_id}'
    match_req = requests.get(target_matchURL,headers=headers)
    # print(match_req.json())
    print(match_req.headers)

else:
    print(req.status_code)



