import os
import json
import base64
from time import sleep as wait

def checkForSave():
    if os.path.exists('data.cash'):
        print("Found save file!\nLoading it atm...\n\n")
        return True

def saveGame(data):
    # 1. Convert python obj to json data
    # 2. Encode the bytes into base64
    # 3. decode the bytes for it to be a string again

    jsonData = json.dumps(data)
    encodedBytes = base64.b64encode(bytes(jsonData, 'utf-8'))
    encodedString = encodedBytes.decode('utf-8')

    with open('data.cash', 'w') as file:
        file.write(encodedString)

# check - load game/return
def loadGame():
        with open('data.cash', 'r') as file:
            encodedData = file.read()
            decodedData = json.loads(base64.b64decode(encodedData))

        return decodedData