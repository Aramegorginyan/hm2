class CustomerAccount:
    def __init__(self, customer_id, customer_name, account_balance):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.account_balance = account_balance
        self.transaction_log = TransactionLog()

    def deposit(self, amount):
        self.account_balance += amount
        transaction_details = f"Deposit: {amount}"
        self.transaction_log.log_transaction(transaction_details)

    def withdraw(self, amount):
        self.account_balance -= amount
        transaction_details = f"Withdrawal: {amount}"
        self.transaction_log.log_transaction(transaction_details)


class TransactionLog:
    def __init__(self):
        self.log = []

    def log_transaction(self, transaction_details):
        self.log.append(transaction_details)

account1 = CustomerAccount(1, "John Doe", 1000)
account2 = CustomerAccount(2, "Jane Doe", 500)

account1.deposit(200)
account1.withdraw(50)
account2.deposit(100)
account2.withdraw(300)
account2.withdraw(200)

print("Account 1 Balance:", account1.account_balance)
print("Account 2 Balance:", account2.account_balance)
print("Transaction Log for Account 2:", account2.transaction_log.log)
