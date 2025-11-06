

print("[Weight Conversion- Kilograms to Stones and Pounds]")
kilograms = float(input("Enter weight in kilograms: "))
pounds = float(kilograms * 2.20462)
stones = int(pounds / 14)
leftoverpounds = float(pounds - stones * 14)
print(f"{kilograms} kilograms is approximately {stones} stones and {round(float(leftoverpounds), 2)} pounds.")