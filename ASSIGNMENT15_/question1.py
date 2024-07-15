class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Example usage:
# Creating an instance of Person
name=input("enter the name=")
age=int(input("enter the age="))
gender=input("enter the gender=")
person1 = Person(name,age,gender)

# Calling the introduce method
person1.introduce()
