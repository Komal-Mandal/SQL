# reverse inheritance is not possible
# main purpose:DRY


class User:

    def login(self):
        print("login")

    def Registration(self):
        print("registration")


class Student(User):

    def enroll(self):
        print("enroll")
        
    def review(self):
        print("review")



stu = Student()

stu.login()
stu.Registration()
stu.enroll()
stu.review()





# when child class don't have it's own constructor parent class constructor is initialized when object of child class is created


class Parent:

    def __init__(self,num,val):
        self.__num = num
        self.val = val

    def get_num(self):
        return self.__num
    

    
class Child(Parent):

        def name(self):
            print("this is the child class")

       


C = Child(100,10)
print(C.get_num())
print(C.name())




"""when child class have their own constructor it initialize it here parent class constructor is not initialize that's way this code give error when we try to print the constructor value of parent class because it is not initialize"""
class Parent:
    
    def __init__(self,num,val):
        self.__num = num
        self.val = val

    def get_num(self):
        return self.__num
    

    
class Child(Parent):

        
    def __init__(self,num,val):
        self.__num = num
        self.val = val

       


C = Child(100,10)
print(C.get_num())

