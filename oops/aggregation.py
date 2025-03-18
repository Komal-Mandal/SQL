class customer:

    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def edit_profile(self,new_name,new_city,new_state,new_pincode):
        self.name = new_name
        self.address.new_address(new_city,new_state,new_pincode)

class address:

    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state 

    def new_address(self,new_city,new_pincode,new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state


add = address("kolkata",382705,"WB")
cus = customer("komal","female",add)

cus.edit_profile("xyz","mumbai","maharastra",123456)

print(cus.address.city)

# here customer has a address class