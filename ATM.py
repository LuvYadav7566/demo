class ATM:
    def __init__(self,pin,balance):
        self.pin = pin
        self.balance = balance
    def menu(self):
        while True:
            print("\n--- Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.check_balance()
            elif choice == '4':
                print("Exiting. Thank you!")
            else:
                print("Invalid choice. Please try again.")
    def deposit(self):
        amount = float(input("Enter amount to deposit:"))
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("invalic amount. Please try again.")
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance: {self.balance}")
        else: 
            print("Insufficient balance or invalid amount. Please try again.")
        
            
    def check_balance(self):
        print(f"Current balance: {self.balance}")
        
account = ATM(pin=1234, balance=500)
account.menu()
            