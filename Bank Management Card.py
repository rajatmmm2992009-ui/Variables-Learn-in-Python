# Bank Management Card

account_holder = "Rajat"
account_number = 1234567890
account_type = "Savings"
balance = 5000
interest_rate = 4.5

deposit_amount = 2500
withdrawal_amount = 1500

balance += deposit_amount
balance -= withdrawal_amount

monthly_interest = balance * (interest_rate / 100)
annual_interest = monthly_interest / 12

print("State Bank of India")
print("=" * 40)
print(f"Account Holder: {account_holder}")
print(f"Account Number: {account_number}")
print(f"Account Type: {account_type}")
print(f"Current Balance: Rs.{balance:.2f}")
print(f"Interest Rate: {interest_rate}%p.a.")
print(f"Monthly Interest: {monthly_interest:.2f}")
print(f"Annual Interest: {annual_interest:.2f}")
