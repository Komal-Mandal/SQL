class customer:

    def __init__(self,name,age):
        self.name = name
        self.age = age

def greed(customer):
    # print(customer.name)
    #print(customer.age)
    print(id(customer)) 
    customer.name = "ankita"
    print(customer.name)
    print(id(customer))



cus = customer("komal",20)
print(id(cus)) 

greed(cus) # object is use as argument
print(cus)

# class object is mutable

# List

