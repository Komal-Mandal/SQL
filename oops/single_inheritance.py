class A:
    
    def __init__(self,name,age):
        print("this is thr parent class constructor")
        self.name = name
        self.age = age

    def intro(self):
        print("this is the parent class constructor")


class B(A):

    def __init__(self,product):
        print("this is the child class")
        self.product = product


b = B("mobile")
print(b.intro())