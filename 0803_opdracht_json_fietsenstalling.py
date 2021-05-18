import json
import requests

stalling = requests.get("https://stallingsnet.nl/api/1/parkingcount/utrecht")
infoStalling = json.loads(stalling.text)

for stalling in infoStalling:

    if stalling["freePlaces"] == 0:

        print(stalling["facilityName"], stalling["freePlaces"], "VOL!!")

    else:

        print(stalling["facilityName"], stalling["freePlaces"])
