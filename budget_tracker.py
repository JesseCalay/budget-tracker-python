balance = 0
transactions = []

def add_transaction(amount, category):
    global balance
    balance += amount
    transactions.append((amount, category))

def show_summary():
    print("\nTransaction Summary:")
    for t in transactions:
        print(f"{'Income' if t[0] > 0 else 'Expense'}: ₱{abs(t[0])} | Category: {t[1]}")
    print(f"\nCurrent Balance: ₱{balance}")

# Example usage
add_transaction(5000, "Salary")
add_transaction(-1500, "Groceries")
add_transaction(-1000, "Transport")
show_summary()
