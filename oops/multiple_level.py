class A:
    
    def buy(self):
            print("buy class A")



class B:

    
    def buy(self):
            print("buy class B")



class C(B,A):

     def buy2(self):
        print("buy class c")

c = C()
c.buy()
