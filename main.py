from threading import Thread
from modules import dataHandler
from modules import codes
from time import sleep as wait

# I hate formatting code

print('''
    Hello, welcome to cash clickers v2 which is a more... Polished version of the game.
    It also has better code so if you want to read it then be my guest!
''')

# dictonary to store all of our variables, this is used for data.
userData = {
    'cash': 0,
    'cashMulti': 1,
    'shop': {
        'price1': 50
    },
    'redeemedCodes': [],
}

# Load data if there is any
if dataHandler.checkForSave():
    userData = dataHandler.loadGame()

# Clear the console
def clear():
    print("\033[2J\033[H", end="", flush=True)

def saveUserData():
    while True:
        wait(10)
        dataHandler.saveGame(userData)

saveThread = Thread(target=saveUserData, daemon=True)
saveThread.start()

# Main game loop
while True:
    print(f'You have ${round(userData['cash'], 2)}')
    userInput = input('Would you like to:\n(ENTER) - Get Cash\n(shop) - Open Shop\n(save) - save the game\n(code) - to redeem a code\n(quit) - quit the game (saves before you do)\n')

    if userInput == '':
        userData['cash'] += 1 * userData['cashMulti']
        clear()
    
    elif userInput.lower() == 'shop':
        isUserDone = False
        while not isUserDone:
            clear()
            userBought = input(f'You have ${userData['cash']}\nWhat would you like to buy?:\n(1) - +1 Multiplier = ${userData['shop']['price1']}\n(leave) - Leave shop\n')

            if userBought.lower() == 'leave':
                print('Goodbye!')
                isUserDone = True
                clear()
            
            # check if user has enough
            elif userBought == '1':
                clear()
                if userData['cash'] >= userData['shop']['price1']:
                    userData['cash'] -= userData['shop']['price1']
                    userData['shop']['price1'] = round(userData['shop']['price1'] * 1.5, 2)
                    userData['cashMulti'] += 1
                    print("Succesfully bought +1 Multiplier")
                    wait(0.4)
                else:
                    clear()
                    print("You dont have enough money... BROKIE LMAOO")
                    wait(0.5)
    
    elif userInput.lower() == "save":
        clear()
        print("Saving...")
        dataHandler.saveGame(userData)

    elif userInput.lower() == "code":
        userData['cash'] += codes.codeScreen(userData['redeemedCodes'])

    elif userInput.lower() == "quit":
        clear()
        dataHandler.saveGame(userData)
        break

print("Goodbye!")
quit()