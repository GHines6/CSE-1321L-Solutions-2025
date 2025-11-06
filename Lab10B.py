
class Dog:
    def __init__(self, age, weight, name, furColor, breed):
        self.age = age
        self.weight = weight
        self.name = name
        self.furColor = furColor
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

    def rename(self, new_name):
        self.name = new_name


    def eat(self, food_weight):
        self.weight += food_weight

print("You are about to create a dog.")
age_in = int(input("How old is the dog: "))
weight_in = float(input("How much does the dog weigh: "))
name_in = input("What is the dog's name: ")
fur_in = input("What color is the dog: ")
breed_in = input("What breed is the dog: ")

d = Dog(age_in, weight_in, name_in, fur_in, breed_in)

print(f"{d.name} is a {d.age} year old {d.furColor} {d.breed} that weighs {d.weight} lbs.")
d.bark()

food_weight = float(input(f"{d.name} is hungry, how much should he eat: "))
d.eat(food_weight)

new_name = input(f"{d.name} isn't a very good name. What should they be renamed to: ")
d.rename(new_name)

print(f"{d.name} is a {d.age} year old {d.furColor} {d.breed} that weighs {d.weight} lbs.")