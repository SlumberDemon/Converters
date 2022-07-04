crypto = ["Bitcoin", "Ethereum", "Tether", "Binance"]
amount = [19095, 1032, 1, 214]

while True:
    choice = input(
        "Type the Crypto currency you wish to convert \n (Bitcoin/Ethereum/Tether/Binance) \n > "
    )
    if choice in crypto:
        value = input("Enter conversion amount \n > ")
        if value.isdigit():
            conversion = int(value) * amount[crypto.index(choice)]
            print(f"$ {value} | {choice} {conversion}")
            break
        else:
            print("[!] Error incorrect value")
    else:
        print("[!] Error crypto currency not available")
