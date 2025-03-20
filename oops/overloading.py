
# python doen't support the methode overloading
# but it is possible by using default value
class student:
  s=0

  def sum(self,a,b):
        s = a+b
        print(s)

  def sum(self,a=None,b=None,c=None):
        
        if a!=None and b!=None and c!=None:
           s= a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s=a
        print(s)


s = student()
print(s.sum(1,2))
     

