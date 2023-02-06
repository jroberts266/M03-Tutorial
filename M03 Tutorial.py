## M03 Tutorial
# Author: Joseph Roberts
# Created: 2023-02-04
# Creating classes and inheiritance

# Creates Pet parent class with attritubes
class Pet:
    def __init__(self, petType, name, age, weight, color, isVaccinated, note):
        self.petType = petType
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.isVaccinated = isVaccinated
        self.note = note

# Creates Dog child class
class Dog(Pet):
    def __init__(self, isNeutered, isSpayed):
        self.isNeutered = isNeutered
        self.isSpayed = isSpayed

# Function that will print dog info  
    def dogRecord(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Color: ", self.color)
        print("Notes: ", self.note)

# Creates Cat child class
class Cat(Pet):
    def __init__(self, isNeutered, isSpayed):
        self.isNeutered = isNeutered
        self.isSpayed = isSpayed

# Function that prints cat info
    def catRecord(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Color: ", self.color)
        print("Notes: ", self.note)

# Pet instances
pet1 = Pet("cat", "maple", "4", "10 lbs","auburn", "yes", "cranky when there are loud noises",)
pet2 = Pet("dog", "Coco", "12", "35 lbs", "White", "Yes", "She is deaf, but can sit and and stay with hand signals")
pet3 = Pet("dog", "Trouble", "22", "40 lbs", "brindle", "No", "Food aggessive, but loves eating hot dogs")

# Calling classes for each instance
pet = Cat.catRecord(pet1)
pet = Dog.dogRecord(pet2)
pet = Dog.dogRecord(pet3)