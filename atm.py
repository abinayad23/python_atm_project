class ATM:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 1000000  # Initial balance
        self.transactions = []

    def check_balance(self):
        print("Your Current Balance is:", self.balance, "Rupees only")

    def deposit(self):
        damount = int(input("Enter your Deposit amount: "))
        self.balance += damount
        self.transactions.append(f"Deposited: {damount}")

    def withdraw(self):
        amount = int(input("Enter the Withdrawal amount: "))
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            print("Transaction Successful")
        else:
            print("Insufficient Balance")

    def transfer(self):
        receiver_id = input("Enter the receiver's user ID: ")
        amount = int(input("Enter the amount to transfer: "))
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Transferred {amount} to {receiver_id}")
            print("Transfer Successful")
        else:
            print("Insufficient Balance")

    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

def main():

    
    print("\nInsert your ATM card")
    user_id = input("Enter your User ID: ")
    pin = input("Enter your PIN: ")
    atm = ATM(user_id,pin)

    while True:
        print("\nATM MENU:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            atm.check_balance()
        elif choice == 2:
            atm.deposit()
        elif choice == 3:
            atm.withdraw()
        elif choice == 4:
            atm.transfer()
        elif choice == 5:
            atm.transaction_history()
        elif choice == 6:
            print("Thank You for using the ATM.")
            break
        else:
            print("Invalid Option")

if __name__== "__main__":
    main()