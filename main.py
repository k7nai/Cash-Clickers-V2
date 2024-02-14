from threading import Thread
from modules import dataHandler
from time import sleep as wait

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
}

# Load data if there is any
if dataHandler.checkForSave():
    userData = dataHandler.loadGame()

# Clear the console
def clear():
    print("\033[2J\033[H", end="", flush=True)

def saveUserData():
    while True:
        wait(60)
        dataHandler.saveGame(userData)

saveThread = Thread(target=saveUserData)
saveThread.start()

# Main game loop
while True:
    print(f'You have ${userData['cash']}')
    userInput = input('Would you like to:\n(ENTER) - Get cash\n(PRESS 1) - Open shop\n(s) - save game\n(q) - quit game\n')

    if userInput == '':
        userData['cash'] += 1 * userData['cashMulti']
        clear()
    
    elif userInput == '1':
        isUserDone = False
        while not isUserDone:
            clear()
            userBought = input(f'You have ${userData['cash']}\nWhat would you like to buy?:\n(1) - +1 Multiplier = $50\n(q) - Leave shop\n')

            if userBought == 'q':
                print('Goodbye!')
                isUserDone = True
                clear()
            
            # check if user has enough
            elif userBought == '1':
                clear()
                if userData['cash'] >= userData['shop']['price1']:
                    userData['cash'] -= userData['shop']['price1']
                    userData['cashMulti'] += 1
                    print("Succesfully bought +1 Multiplier")
                    wait(1)
                else:
                    clear()
                    print("You dont have enough money... BROKIE LMAOO")
                    wait(1)
    
    elif userInput == "s":
        clear()
        print("Saving...")
        dataHandler.saveGame(userData)

    elif userInput == "q":
        clear()
        print("Goodbye!")
        dataHandler.saveGame(userData)
        break

saveThread.join()