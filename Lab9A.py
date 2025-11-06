
def allMath(a,b):
    if b == 0:
        division = None
        modulus = None
        floor = None
    else:
        division = a/b
        floor = a//b
        modulus = a%b
    return a+b, a-b, a*b, division, floor, modulus, a**b
first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))
result = allMath(first,second)
print(f"Your resulting tuple is {result}")