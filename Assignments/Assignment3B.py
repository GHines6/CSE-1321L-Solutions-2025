
print("[Sum of Unique Products of Pairs]")
num = int(input("Enter a number: "))
n1 = 1
n2 = 0
UniqueSum = 0
while n1 != num or n2 != num:
    if n2 != num:
        n2 += 1
    else:
        n2 = 1
        n1 += 1
    product = n1 * n2
    duplicate = False
    a = 1
    while a <= n1:
        b = 1
        while b <= num:
            if a == n1 and b >= n2:
                break
            if a * b == product:
                duplicate = True
                break
            b += 1
        if duplicate:
            break
        a += 1
    if duplicate:
        print(f"({n1},{n2})={product} (duplicate, ignore)")
    else:
        print(f"({n1},{n2})={product}")
        UniqueSum += product
print(f"Sum of unique products: {UniqueSum}")

