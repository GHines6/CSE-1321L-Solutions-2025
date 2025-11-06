# Class: CSE 1321L
# Section: 01
# Term: Fall 2025
# Instructor: Michael Butler
# Name: Giovanni Hines
# Lab#: 3A

AmountOwed = float(input("Amount owed: $"))
AnnualPercentageRate = float(input("APR: "))
MonthlyPercentageRate = float(float(AnnualPercentageRate) / 12)
MinimumPayment = float(AmountOwed * MonthlyPercentageRate / 100)
print(f"Monthly percentage rate: {round(float(MonthlyPercentageRate), 3)}")
print(f"Minimum payment: ${round(float(MinimumPayment), 2)}")
