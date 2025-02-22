# # base class

# class Animal:
#     def __init__(self,name):
#         self.name = name 
    
#     def speak(self):
#         print(f"{self.name} makes a sound ")
    
# # Derived class

# class Dog(Animal):
#     # def speak(self):
#     #     print(f"{self.name} barks")# here constructr for the child class is not defined 
#         # so it is using only the parent class constructor 
#     # def speak1(self):
#     #     print(f"{self.name} barrks")
#     def __init__(self):
#         self.behaviour = 'friendly'
#     def speak(self):
#         print(f"{self.name} barrks and he is very {self.behaviour}")
#         # print(f"Routell barrks and he is very {self.behaviour}")

# animal = Animal("Generic")
# animal.speak() # parent clas object

# Child class object
# dog =Dog("Routella") #it is using only the parent class constructor so we have to pass an argument
# dog.speak() 
# child method override the parent method / or you can inherit the parent method
# dog.speak1()

# constructor overloading and over riding
# dog =Dog() # since we have defined the dog class constructor it dont need any argument
# dog.speak()
# to also inherit the attribute the animal character we have to use super key 
#*************Super key word**********
# base class

class Animal:
    def __init__(self,name):
        self.name = name 
    
    def speak(self):
        print(f"{self.name} makes a sound ")
    
# Derived class

class Dog(Animal):
    def __init__(self,behaviour):
        super().__init__("routella")# argument needed to animal class
        self.behaviour = behaviour
    def speak(self):
        super().speak() # way to call the base class funtion in child class
        print(f"{self.name} barrks and he is very {self.behaviour}")
        # print(f"Routell barrks and he is very {self.behaviour}")
dog=Dog('friendly')
dog.speak()

