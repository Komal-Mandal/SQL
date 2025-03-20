# import ABC from abd ,abstract class should have to inheritate ABC class and inside the class atlest one method should be abstract method 



from abc import ABC,abstractclassmethod

class BankApp(ABC):

    def database(self):
        print("database info")
   
    @abstractclassmethod
    def security(self):
        pass


class WebApp(BankApp):
    
    def login(self):
        print("this is for login")

    def security(self):
        print("this is for security")




w = WebApp()