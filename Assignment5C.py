
running, letterloop, numberloop = True, False, False
letterlist = []
numberlist = []
numbertuple = ()
lettertuple = ()
maxfreq = -1
def find_frequency(data):
    frequency = {}
    for ch in data:
        frequency[ch] = frequency.get(ch, 0) + 1
    return frequency
while running:
    print("Main Menu\n1. Enter letters\n2. Enter numbers\n3. Quit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            letterlist = []
            maxkeys = []
            letters = input("Enter letters separated by commas: ")
            for i in letters:
                if i != ",":
                    letterlist.append(i)
            lettertuple = tuple(letterlist)
            alphadict = find_frequency(lettertuple)
            for key, value in alphadict.items():
                if value > maxfreq:
                    maxfreq = value
                    maxkeys = [key]
                elif value == maxfreq:
                    maxkeys.append(key)
            print(f"Tuple: {lettertuple}")
            print(f"Frequency dictionary: {alphadict}")
            print(f"Most frequent element(s): ", end="")
            print(*maxkeys, sep=", ")
            print(f"Frequency: {maxfreq}")
            maxfreq = -1

        case 2:
            numberlist = []
            maxkeys = []
            numbers = input("Enter numbers separated by commas: ")
            for i in numbers:
                if i != ",":
                    numberlist.append(int(i))
            numbertuple = tuple(numberlist)
            numdict = find_frequency(numbertuple)
            for key, value in numdict.items():
                if value > maxfreq:
                    maxfreq = value
                    maxkeys = [key]
                elif value == maxfreq:
                    maxkeys.append(key)
            print(f"Tuple: {numbertuple}")
            print(f"Frequency dictionary: {numdict}")
            print(f"Most frequent element(s): ", end="")
            print(*maxkeys, sep=", ")
            print(f"Frequency: {maxfreq}")
            maxfreq = -1
        case 3:
            print("Exiting program...")
            break
    print()
