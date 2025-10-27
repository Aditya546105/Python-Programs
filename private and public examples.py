class BankAccount:
    def __init__(self, account_holder, balance):
        # public attribute
        self.account_holder = account_holder
        
        # private attribute (prefix with __)
        self.__balance = balance

    # public method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # public method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    # private method
    def __show_balance(self):
        print(f"Your current balance is ₹{self.__balance}")

    # public method to access private method safely
    def check_balance(self):
        self.__show_balance()


# --- Using the class ---
account = BankAccount("Aditya", 5000)

# Accessing public attribute
print("Account Holder:", account.account_holder)

# Using public methods
account.deposit(2000)
account.withdraw(1000)
account.check_balance()

# Trying to access private attribute directly (will cause error)
# print(account.__balance)  # ❌ AttributeError

# Correct way to access private data (through public method)
account.check_balance()
