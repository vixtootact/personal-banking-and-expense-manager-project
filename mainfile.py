data_file = "bank_data.txt"

def load_data():
    try:
        file = open(data_file, "r")
        lines = file.readlines()
        file.close()
        name = lines[0].strip()
        balance = float(lines[1].strip())
        expenses = []
        for line in lines[2:]:
            description, category, amount = line.strip().split("|")
            expenses.append({
                "description": description,
                "category": category,
                "amount": float(amount)
            })
        return name, balance, expenses
    except FileNotFoundError:
        return None, 0, []
    except Exception as error:
        print("Error loading data:", error)
        return None, 0, []
    

def save_data(name, balance, expenses):
    try:
        file = open(data_file, "w")

        file.write(name + "\n")
        file.write(str(balance) + "\n")

        for expense in expenses:
            file.write(
                f"{expense['description']}|"
                f"{expense['category']}|"
                f"{expense['amount']}\n"
            )

            file.close()
            print("Data saved successfully.")

    except Exception as error:
        print("Error saving data:", error)


def create_account():
    print("\n===== CREATE ACCOUNT =====")
    name = input("Enter your name: ")

    while True:
        try:
            balance = float(input("Enter starting balance: "))

            if balance < 0:
                print("Balance cannot be negative.")
                continue

            return name, balance

        except ValueError:
            print("Please enter a valid amount.")

#Check balance function

def check_balance(balance):
    print(f"\nCurrent balance: {balance:.2f}")

#Deposit function

def deposit(balance):
    try:
        amount = float(input("Enter amount to deposit: n"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return balance
        balance += amount
        print(f"n{amount:.2f} deposited successfully.")

    except ValueError:
        print("Invalid amount.")

# WITHDRAW FUNCTION

def withdraw(balance):
    try:

        amount = float(input("Enter amount to withdraw: n"))

        if amount <= 0:
            print("Amount must be greater than zero.")

        elif amount > balance:
            print("Insufficient balance.")

        else:
            balance -= amount
            print(f"n{amount:,.2f} withdrawn successfully.")

    except ValueError:
        print("Invalid amount.")
    return balance

# add expense function

def add_expense(expenses, balance):
    try:
        description = input("Expense description: ")
        category = input("Category: ")
        amount = float(input("Amount: n"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return balance
        
        if amount > balance:
            print("Not enough balance.")
            return balance
        
        expense = {
            "description": description,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        balance -= amount
        print("Expense added successfully.")
        
    except ValueError:
        print("Invalid amount.")
    return balance
