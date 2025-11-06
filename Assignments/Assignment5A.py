
def myselectionsort(list):
    indexing_length = range(0, len(list)-1)
    for i in indexing_length:
        min_value = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_value]:
                min_value = j
        if min_value != i:
            list[i], list[min_value] = list[min_value], list[i]
    return list
numbers = input("Enter numbers separated by commas: ")

numlist = []
for char in numbers.split(","):
    if char:
        numlist.append(int(char))
sortednum = sorted(numlist)
mysort = myselectionsort(numlist.copy())
print(f"Original list: {numlist}")
print(f"Sorted list (using my selection sort): {mysort}")
print(f"Sorted list (using default function): {sortednum}")
if mysort != sortednum:
    print("The lists are not the same.")
else:
    print("Both lists are identical!")
