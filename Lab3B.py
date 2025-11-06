# Class: CSE 1321L
# Section: 01
# Term: Fall 2025
# Instructor: Michael Butler
# Name: Giovanni Hines
# Lab#: 3B

Course1Hours = int(input("Course 1 hours: "))
Course1Grade = int(input("Grade for course 1: "))
Course2Hours = int(input("Course 2 hours: "))
Course2Grade = int(input("Grade for course 2: "))
Course3Hours = int(input("Course 3 hours: "))
Course3Grade = int(input("Grade for course 3: "))
Course4Hours = int(input("Course 4 hours: "))
Course4Grade = int(input("Grade for course 4: "))
TotalHours = Course1Hours + Course2Hours + Course3Hours + Course4Hours
Quality1 = Course1Hours * Course1Grade
Quality2 = Course2Hours * Course2Grade
Quality3 = Course3Hours * Course3Grade
Quality4 = Course4Hours * Course4Grade
TotalQualityPoints = int(Quality4 + Quality3 + Quality1 + Quality2)
GPA = float(Quality4 + Quality3 + Quality1 + Quality2) / TotalHours

print(f"Total hours: {TotalHours}")
print(f"Total quality points: {TotalQualityPoints}")
print(f"Your GPA for this semester is {round(float(GPA),2)}")
