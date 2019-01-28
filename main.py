import requests
import time
from pypresence import Presence
from datetime import datetime, timedelta
client_id = '535883147112611880'
RPC = Presence(client_id)  # Initialize the client class
RPC.connect()  # Start the handshake loop
ip = str('http://localhost')
port = str(8080)  # By default the port is 8080 if you have changed it specify here
url = str(ip) + ':' + str(port) + '/jsonrpc'
infourl = "?request={%20%22jsonrpc%22:%20%222.0%22,%20%22method%22:%20%22Player.GetItem%22,%20%22params%22:%20{%20%22properties%22:%20[%20%22title%22,%20%22season%22,%20%22episode%22,%20%22duration%22,%20%22showtitle%22,%20%22tvshowid%22],%20%22playerid%22:%201%20},%20%22id%22:%20%22VideoGetItem%22%20}"
lengthurl = "?request={%22jsonrpc%22:%222.0%22,%22method%22:%22Player.GetProperties%22,%22params%22:{%22playerid%22:1,%22properties%22:[%22speed%22,%22time%22,%22totaltime%22]},%22id%22:%221%22}"
result = None


def loading(string):
    for x in range(0, 6):
        b = string + "." * x
        print(b, end="\r")
        time.sleep(1)


def set_rp(info, length):
    info = info['result']['item']
    length = length['result']
    start_time = (datetime.now() - timedelta(hours=length["time"]['hours'], minutes=length["time"]['minutes'], seconds=length["time"]['seconds']))
    end_time = (start_time + timedelta(hours=length['totaltime']['hours'], minutes=length['totaltime']['minutes'], seconds=length['totaltime']['seconds'])).timestamp()
    start_time = start_time.timestamp()

    if info['type'] == 'movie':
        if length['speed'] == 0:
            RPC.update(details=str(info['title']),
                       state="Paused...",
                       large_image='kodi_dark',
                       large_text='Kodi Rich Prescence by Alphex#0977',
                       small_image='pause',
                       small_text='Paused')
        else:
            RPC.update(details=str(info['title']),
                       start=start_time,
                       end=end_time,
                       large_image='kodi_dark',
                       large_text='Kodi Rich Prescence by Alphex#0977',
                       small_image='play',
                       small_text='Playing')

    if info['type'] == "episode":
        state_info = 'Season ' + str(info['season'])+' Episode ' + str(info['episode'])+' : ' + str(info['title'])

        if length['speed'] == 0:
            RPC.update(state=state_info,
                       details=str(info['showtitle']),
                       start=start_time,
                       end=end_time,
                       large_image='kodi_dark',
                       large_text='Kodi Rich Prescence by Alphex#0977',
                       small_image='pause',
                       small_text='Paused')
        else:
            RPC.update(state=state_info,
                       details=str(info['showtitle']),
                       start=start_time,
                       end=end_time,
                       large_image='kodi_dark',
                       large_text='Kodi Rich Prescence by Alphex#0977',
                       small_image='play',
                       small_text='Playing')

    if info['type'] == 'unknown':
        RPC.update(state="Not watching anything",
                   details="IDLE",
                   large_image='kodi_dark',
                   large_text='Kodi Rich Prescence by Alphex#0977',
                   small_image='pause',
                   small_text='Nothing Playing')

    time.sleep(15)


while True:
    try:
        info = requests.get(url+infourl).json()
        length = requests.get(url+lengthurl).json()
        set_rp(info, length)
    except requests.exceptions.RequestException:
        print("Cant connect to Kodi web interface. Are you sure its running? Is the web interface on?")
        loading("Trying again in 5 seconds")
        pass
