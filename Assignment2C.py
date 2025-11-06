
total = 0
count = 0
num = ""
temp = input("Enter temperatures in F (separate them with ,): ")
for char in temp + ",": #this gets the last number when I enter it by putting a comma after it so the if statement reads it
    if char != ",":
        num += char
    else:
        total += float(num)
        count += 1
        num = ""
print(f"You've entered {count} temperature points.")
avg = total/count if count else 0
print(f"The average temperature is {avg:.2f}F")
