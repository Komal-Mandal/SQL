class Atm:
    """Constructor: The code inside the constructor runs automatically when an object is created."""

    # Method: A function inside a class is called a method.
    
    def __init__(self):
        self.pin = ""
        self.balance = 0
        print(id(self))
        self.menu()
       

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
        self.pin = input("Enter a new PIN: ")
        print("PIN created successfully!")

    def deposit(self):
        temp = input("enter you pin")
        if temp == self.pin:
            amount = float(input("Enter amount to deposit: "))
            self.balance += amount
            print(f"₹{amount} deposited successfully! New balance: ₹{self.balance}")

    def withdraw(self):
        temp = input("enter you pin")
        if temp == self.pin:
            amount = float(input("Enter amount to withdraw: "))
            print(amount)
            if amount > self.balance:
              print("Insufficient balance!")
            else:
               self.balance -= amount
               print(f"₹{amount} withdrawn successfully! Remaining balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")



sbi = Atm()
print(id(sbi))


