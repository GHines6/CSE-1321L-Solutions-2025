
def validate(message, offset):
    letters = False
    for ch in message:
        if ch.isalpha() or ch.isspace():
            letters = True
        else:
            letters = False
            break
    if 0 <= offset <= 26 and letters:
        return True
    else:
        return False
def encrypt(message, offset):
    encrypted = ""
    message = message.upper()
    for ch in message:
        if ch == " ":
            encrypted += " "
        else:
            encrypted += chr((ord(ch) - 65 + offset) % 26 + 65)
    return encrypted
run = True
while run:
    message = input("Enter your message:\n")
    offset = int(input("Enter the offset value: "))
    print()
    validation = validate(message, offset)
    if validation:
        print(f"Your secret message is...\n{encrypt(message, offset)}")
    else:
        print("Sorry, we can only process messages with letters and spaces, and the offset must be between 0 and 26.")
    print()
    dorun = input("Do you want to encrypt another message? (Y/N): ")
    print()
    if dorun == "Y":
        pass
    else:
        run = False
        print("Closing out...")