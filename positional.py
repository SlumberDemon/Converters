def convert(num: int):
    return str(num) + (
        "th"
        if 4 <= num % 100 <= 20
        else {1: "st", 2: "nd", 3: "rd"}.get(num % 10, "th")
    )


while True:
    value = input("Enter number to convert to positional number \n > ")
    if value.isdigit():
        print(f"Positional number: {convert(int(value))}")
        break
    else:
        print("[!] Make sure you input a number")
