# #EXAMPLE-1
# class Sagarmatha:
#     def __init__(self):           #Constructor
#         print("This is for CONSTRUCTOR")
#     def home1(self):               #Normal Function, can be accessed by all
#         print("Sweet home")
#     def classcall():                #Normal function, only its class can call
#         print("No self required")
#     def __del__(self):
#         print("This is for DESTRUCTOR")

# #Calling using Class
# Sagarmatha.classcall()

# #Calling using object
# sg = Sagarmatha()        #sg is object
# sg.home1()


# #EXAMPLE-2 (PASSING ARGUMENTS MAKING OBJECT)
# class Sanepa:
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address
#     def abc(self,rollno):    
#         print(f"My rollno is {rollno} age is {self.age}. I live in {self.address}")
#         print(self.age)
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.address)

# obj1 = Sanepa("Swornima",20,"Dhumbarahi")
# obj2 = Sanepa("Binayak",21,"Thamel")
# obj1.display()
# obj2.display()
# obj1.abc("046")


# #EXAMPLE-3
# class Visualization:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def homie(self):
#         print(self.name,self.age)

# viz = Visualization("Dakshita",6)
# viz.homie()

# #EXAMPLE-4 (Inheritance)
# class Sagarmatha:
#     def __init__(self,no_of_department = 2, no_of_students = 1000,no_of_faculty = 100):
#         self.affiliation = "T.U."
#         self.no_of_department = no_of_department
#         self.location = "Sanepa"
#         self.no_of_students = no_of_students
#         self.no_of_faculty = no_of_faculty
    
#     def canteen_profit(self):
#         return self.no_of_students * 0.1*10

# class ScienceTechnology(Sagarmatha):
#     def __init__(self,no_of_department = 2, no_of_students = 1000,no_of_faculty = 100):
#         super().__init__(no_of_department, no_of_students, no_of_faculty)
#         self.affiliation = "P.U."
#         self.no_of_department = no_of_department
#         self.location = "Kathmandu"
#         self.no_of_stuedents = no_of_students
#         self.no_of_faculty = no_of_faculty
    
#     def canteen_loss(self):
#         return self.no_of_students * 0.2*10

# obj = ScienceTechnology()
# print(obj.canteen_profit())    #prints the profit of class Sagarmatha

##EXAMPLE-5(inheritance)
# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def make_sound(self):
#         print("Some animal sound")
       
        
# class Dog(Animal):
#     def make_sound(self):
#         super().make_sound()
#         print("Woof!")
    
# dog = Dog("Max")
# print(dog.name)
# dog.make_sound()

#EXAMPLE-6 (POLYMORPHISM)


# #EXAMPLE-7(DATA HIDING)
# class Car:
#     def __init__(self, make, model, year):
#         self.__make = make
#         self.__model = model
#         self._year = year
        
#     def get_make(self):
#         return self.__make
    
#     def get_model(self):
#         return self.__model
    
#     def get_year(self):
#         #protected
#         return self._year
    
#     def set_make(self, make):
#         self.__make = make
        
#     def set_model(self, model):
#         self.__model = model
        
#     def set_year(self, year):
#         self._year = year
        
# car = Car("Toyota", "Camry", 2022)
# print("Make:", car.get_make())
# print("Model:", car.get_model())
# car.set_year(2021)
# print("Year:", car.get_year())

##EXPLANATION::
## In this example, we have a class Car that represents a car object. The class has three attributes: __make, __model, and __year, which store the make, model, and year of the car, respectively.

# #Access to the attributes is controlled through methods get_make, get_model, and get_year, which return the values of the corresponding attributes. The attributes can also be modified through methods set_make, set_model, and set_year.

# #Notice that the attributes have names that start with double underscores, which makes them private. This means that they cannot be directly accessed from outside the class. Instead, they can only be accessed through the methods.

# #This demonstrates how encapsulation allows you to hide the implementation details of an object and control access to its attributes, making it easier to maintain and change the implementation over time.