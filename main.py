import requests, time, json

f = open('config.json', 'r')
data = json.load(f)

USERID = data['UserID']
SERVERID = data['ServerID']
CHANNELID = data['ChannelID']
CHANNELID1 = data['ChannelID1']
CHANNELID2 = data['ChannelID2']
CHANNELID3 = data['ChannelID3']
CHANNELID4 = data['ChannelID4']
CHANNELID5 = data['ChannelID5']
TOKEN = data['token']

channel = [CHANNELID, CHANNELID1, CHANNELID2, CHANNELID3, CHANNELID4, CHANNELID5]
count = 0
while True:
    for channelid in channel:
        if count == 10:
            time.sleep(10)

        moove = requests.patch(f'https://discord.com/api/v9/guilds/{SERVERID}/members/{USERID}', json={"channel_id": f"{channelid}"}, headers={"authorization": TOKEN, "accept-encoding": "gzip, deflate, br", "content-type": "application/json", "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36"})
        if moove.status_code == 200:
            print("User Mooved With Succes")
            count += 1
        else:
            print(moove.text)
            print("CANT MOOVE FUCKING USER")
