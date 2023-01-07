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

#EXAMPLE-4 (Inheritance)
class Sagarmatha:
    def __init__(self,no_of_department = 2, no_of_students = 1000,no_of_faculty = 100):
        self.affiliation = "T.U."
        self.no_of_department = no_of_department
        self.location = "Sanepa"
        self.no_of_students = no_of_students
        self.no_of_faculty = no_of_faculty
    
    def canteen_profit(self):
        return self.no_of_students * 0.1*10

class ScienceTechnology(Sagarmatha):
    def __init__(self,no_of_department = 2, no_of_students = 1000,no_of_faculty = 100):
        super().__init__(no_of_department, no_of_students, no_of_faculty)
        self.affiliation = "P.U."
        self.no_of_department = no_of_department
        self.location = "Kathmandu"
        self.no_of_stuedents = no_of_students
        self.no_of_faculty = no_of_faculty
    
    def canteen_loss(self):
        return self.no_of_students * 0.2*10

obj = ScienceTechnology()
print(obj.canteen_profit())    #prints the profit of class Sagarmatha
