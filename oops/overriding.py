class A:
    def name(self):
      print("this is class A")


class B(A):
   def name(self):
      print("this is the class B")


a = B()
print(a.name())