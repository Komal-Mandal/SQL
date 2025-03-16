# nothing is truely private in python


class Atm:
    """ATM class with private attributes and proper encapsulation."""

    def __init__(self):
        self.__pin = ""  # Private attribute
        self.__balance = 0  # Private attribute
        print(id(self))
        self.menu()

      
    def get_pin(self):
        return self.__pin
    

    
    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN was changed successfully!")
        else:
            print("Invalid PIN! Please enter a 4-digit numeric PIN.")
        
    def menu(self):
        while True:
            user_input = input("""
            Hello, how would you like to proceed?
            Enter 1 to create pin
            Enter 2 to deposit
            Enter 3 to withdraw
            Enter 4 to check balance
            Enter 5 to exit
            """)

            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()
            elif user_input == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid input. Please try again.")

    def create_pin(self):
        self.__pin = input("Enter a new PIN: ")
        print("PIN created successfully!")

    def deposit(self):
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            amount = float(input("Enter amount to deposit: "))
            self.__balance += amount
            print(f"₹{amount} deposited successfully! New balance: ₹{self.__balance}")
        else:
            print("Incorrect PIN!")

    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            amount = float(input("Enter amount to withdraw: "))
            if amount > self.__balance:
                print("Insufficient balance!")
            else:
                self.__balance -= amount
                print(f"₹{amount} withdrawn successfully! Remaining balance: ₹{self.__balance}")
        else:
            print("Incorrect PIN!")

    def check_balance(self):
        print(f"Your current balance is: ₹{self.__balance}")  # Fixed access

    # Getter for private balance
    def get_balance(self):
        return self.__balance

    # Setter to update private balance (if needed)
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative!")


# Creating an ATM instance
sbi = Atm()
print(id(sbi))


# sbi.__balance = "xyz"  # This won't actually modify the private attribute

# sbi.set_pin("4567")

sbi.get_pin()




