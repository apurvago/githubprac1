# Question - multi-path 
class LandVehicle:
    #instance attribute
    def __init__(self, name):
        self.name=name
    #Method
    def drive(self):
        print(f"{self.name} is moving on land")

class WaterVehicle:
    #instance attribute
    def __init__(self, name):
        self.name=name
    #Method
    def sail(self):
        print(f"{self.name} is moving on water")
    
class AmphibiousVehicle(LandVehicle,WaterVehicle):
    #instance attribute
    def __init__(self, name, propulsion_type):
        self.name=name
        self.propulsion_type=propulsion_type
    #Method
    def travel(self):
        print(f"{self.name} is using {self.propulsion_type} for propulsion")
        self.drive()       #call parents method here
        self.sail()

amphibious_vehicle = AmphibiousVehicle("hovercraft","wheels")     #inverted commas
amphibious_vehicle.travel() 
      




#Question 2 - overriding 

class Shape():
    pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return 3.142* self.radius* self.radius
    
class Rectangle(Shape):
    def __init__(self, l, w):
        self.l=int(l)
        self.w=int(w)
    def area(self):
        return self.l* self.w
    
circle = Circle(4)
rectangle= Rectangle(4,5)

print(f"Area of circle: {circle.area()}")
print(f"Area of rectangle: {rectangle.area()}")




# Question 3 - multiple inheritance 
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):       #self inside the brackets 
        print(f"{self.name} and age is {self.age}")

class Teacher(Person):
    def __init__(self,name,age,role):
        Person.__init__(self,name,age)
        self.role=role
    def display(self): 
        print(f"Teacher Info: {self.name} and age is {self.age} and she is a {self.role}")
        

class Student(Person):
    def __init__(self,name,age,role):
        Person.__init__(self,name,age)
        self.role=role
    def display(self):
        print(f"Student Info: {self.name} and age is {self.age} and she is a {self.role}")

student=Student('Apurva','23','Student')
teacher=Teacher('Aparna','50','Teacher')

student.display()
teacher.display()
          
    
#Q3  overloading and overridding:

class Shape():
    def area():
        return 0

class Circle(Shape):
    def __init__(self,radius):
        self.radius=float(radius)
    def area(self):
        Shape.area()
        return 3.142*self.radius*self.radius
    
class Rectangle(Shape):
    def __init__(self,l,w):
        self.l=float(l)
        self.w=float(w)
    def area(self):
        Shape.area()
        return self.l*self.w
    
circle=Circle(8.1425056)
rec=Rectangle(5.35698789,9.17849613)

print(f"Area of circle is {circle.area()}")
print(f"Area of rectangle is {rec.area()}")



# Q4: Encapsulation   ??????????????????? CHECK AGAINNNNNN

"""class BankAccount():
    def __init__(self,balance):
        self.balance=0.0
    def deposit(self,amount):
        self.amount=float(amount)
    def withdraw(self,amount):
        self.amount=float(amount)
    def get_balance(self):
        return float(self.deposit) - float(self.withdraw)

transac=BankAccount(1958753)
transac.get_balance(print(f'The balance is: {transac.get_balance}'))"""


# Question: Abstraction 

from abc import ABC, abstractmethod  #import
class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title=title
        self.item_id=item_id
    @abstractmethod
    def check_out(self):
        pass 
    @abstractmethod
    def return_item(self):
        pass
    @abstractmethod
    def display(self):
        pass

class Book(LibraryItem):
    def __init__(self,title,item_id,author,genre):
        LibraryItem().__init__(title, item_id)
        self.author=author
        self.genre=genre
        self.checked_out=False
    def check_out(self):
        if not self.checked_out:
         return f"The book '{self.title}' has been checked out."
        else:
         return "This book is already checked out"
    
    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"The book '{self.title}' has been returned."
        else:
            return "This book is not currently checked out."
    def display(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}" 


class DVD(LibraryItem):
    def __init__(self,director,duration):
        self.director=director
        self.duration=int(duration)
    def check_out(self):
        pass
    def return_item(self):
        pass
    def display(self):
        pass

book=Book('Hamlet','601','William Shakespeare','Classic Literature')
book=Book('Who will cry when you will die?','978','Robin Sharma','Self-help')

dvd=DVD('Tale of India','9876','Rashtra J','60')
dvd=DVD('Marathi Classics','1265','Dr.A.Kuber','150')



# Midsem  - employee 
class Employee():
    def __init__(self,employee_id,name):
        self.employee_id=employee_id
        self.name=name
    def set_Age(self):
        self.set_Age=23
        return self.set_Age
    def set_Salary(self):
        self.salary=120000
        return self.salary
    def display(self):
        print("The employee id is :"+str(self.employee_id))
        print("The name is :"+self.name)
        print("The age is :"+str(self.set_Age))
        print("The salary is :"+str(self.salary))
obj=Employee(123,'Radha')
obj.set_Age()
obj.set_Salary()
obj.display()


# midterm 
class Tree:
    Treecode=0
    height=0
    base=0
    amount_tree=0
    
    def _init_(self,tc,h,b,amt):
        self.Treecode=tc
        self.height=h
        self.base=b
        self.amount_tree=amt
    def display(self):
        print("the treecode is :"+str(self.Treecode))
        print("the height of tree is :"+str(self.height))
        print("the base of tree is : "+str(self.base))
        print("the amount spent on tree is : "+str(self.amount_tree))
        
    def update(self):
        self.Treecode=int(input("Update the Treecode :"))
        self.height=int(input("Update the height of tree :"))
        self.base=int(input("Update the base of tree :"))
        self.amount_tree=(int(input("Update the amount spent on tree :")))
        return self.Treecode,self.height,self.base,self.amount_tree
    
class Garden(Tree):
    MangoTree=Tree(12,36,11,12000)
    MangoTree.display()
    MangoTree.update()