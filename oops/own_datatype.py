# custom datatype
# magic method
# this methods are run automatically with specific condition


class Fraction:

    def __init__(self,n,d):
        self.num = n
        self.dun = d

    def __str__(self):
        return "{}/{}".format(self.num,self.dun)
    
    def __add__(self,other):
        temp_num = self.num*other.dun + self.dun*other.num
        temp_dun = self.dun*other.dun
        return "{}/{}".format(temp_num,temp_dun)
    
    def __sub__(self,other):
        temp_num = self.num*other.dun - self.dun*other.num
        temp_dun = self.dun*other.dun
        return "{}/{}".format(temp_num,temp_dun)
    
    def __mul__(self,other):
        temp_num = self.num*other.num 
        temp_dun = self.dun*other.dun
        return "{}/{}".format(temp_num,temp_dun)
    
    def __truediv__(self,other):
        temp_num = self.num*other.dun
        temp_dun = self.dun*other.num
        return "{}/{}".format(temp_num,temp_dun)




x = Fraction(2,3)
y = Fraction(4,5)
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)