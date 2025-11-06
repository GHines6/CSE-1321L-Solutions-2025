
nospace = ""
print("[Welcome to the Letter Frequency Quiz]")
sentence = input("Enter a sentence (lowercase letters only): ")
for letter in sentence:
    if letter != " ":
        nospace += letter
repeat = ""
for char in nospace:
    if char in repeat:
        continue
    frequency = 0
    for c in nospace:
        if c == char:
            frequency += 1
    while True:
        guess = int(input(f"Guess the frequency of letter '{char}': "))
        if guess > frequency:
            print("Too high!")
        elif guess < frequency:
            print("Too low!")
        else:
            print("Correct!")
            break
    repeat += char
print("Congratulations! You completed the quiz.")


