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


#EXAMPLE-2 (PASSING ARGUMENTS MAKING OBJECT)
class Sanepa:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def abc(self,rollno):    
        print(f"My rollno is {rollno} age is {self.age}. I live in {self.address}")
        print(self.age)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.address)

obj1 = Sanepa("Swornima",20,"Dhumbarahi")
obj2 = Sanepa("Binayak",21,"Thamel")
obj1.display()
obj2.display()
obj1.abc("046")