monthly_incomes = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expense: "))
monthly_savings = monthly_incomes - monthly_expenses
projected_saving = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected saving after one year , with interest, is: {projected_saving}.")