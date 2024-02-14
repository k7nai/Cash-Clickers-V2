import os
import json
import base64
from time import sleep as wait

# clear the console
def clear():
    print("\033[2J\033[H", end="", flush=True)

def checkForSave():
    if os.path.exists('data.cash'):
        print("Found save file!\nLoading it atm")
        return True

def saveGame(data):
    clear()
    print("Saving game please wait...")
    # 1. Convert python obj to json data
    # 2. Encode the bytes into base64
    # 3. decode the bytes for it to be a string again

    jsonData = json.dumps(data)
    encodedBytes = base64.b64encode(bytes(jsonData, 'utf-8'))
    encodedString = encodedBytes.decode('utf-8')

    with open('data.cash', 'a+') as file:
        file.write(encodedString)
    
    print("Game saved!")
    wait(1)
    clear()

# check - load game/return
def loadGame():
        with open('data.cash', 'r') as file:
            encodedData = file.read()
            decodedData = json.loads(base64.b64decode(encodedData))
        clear()

        return decodedData