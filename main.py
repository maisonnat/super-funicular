import requests
import json

#Request URL: https://discord.com/api/v9/guilds/837370613521842216/messages/search?channel_id=837370614243000345

#Hay que verificar como hacer el timestep
#https://discord.com/api/v9/guilds/837370613521842216/messages/search?channel_id=837370614243000345&content=spawnvehicles


token_authorization = 'aca va el token' #COMPLETAR CON EL TOKEN https://www.androidauthority.com/get-discord-token-3149920/

def retrive_messages(channelid):
    headers = {
        'authorization': token_authorization
    }

    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        print(value['content'],'\n')


def search_messages(channelid):
    headers = {
        'authorization': token_authorization
    }

    r = requests.get(f'https://discord.com/api/v9/guilds/837370613521842216/messages/search?channel_id={channelid}&content=spawnvehicles', headers=headers)
    jsonn = json.loads(r.text)
    pretty = json.dumps(jsonn, indent=4)
    print(pretty)
    #for messages in jsonn['messages']:
        #print(messages['content'],'\n')


#retrive_messages('837370614243000345')
search_messages('837370614243000345')