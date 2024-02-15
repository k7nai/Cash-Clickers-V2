from time import sleep

codes = {
    "firstrelease": 1000,
}

# Clear the console
def clear():
    print("\033[2J\033[H", end="", flush=True)

# Check to see if code is on list, returns the amount of money. return 0 to not get a NoneType
def codeScreen(redeemed):
    code = input("Please enter a code!: ")

    if code.lower() in codes and code.lower() not in redeemed:

        print(f"\n\nSuccesfully redeemed code for ${codes[code.lower()]}\n")
        redeemed.append(code.lower())

        sleep(1)
        return codes[code.lower()]
    else:
        print("\n\nSorry, but that's not a code on the list OR you have already claimed this code.\n")
        return 0