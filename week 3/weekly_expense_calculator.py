print("=========================================")
print("student_weekly_expense_calcultor_15875")
print("=========================================")
print()
name = input("Student Name; ")
transport_cost = float(input("Enter daily transport cost; "))
feeding_cost = float(input("Enter daily feeding cost; "))
campus_days = float(input("Enter the number of days on campus; "))
other_expenses = float(input("Enter other weekly expenses; ")) 
budget = float(input("Enter the value of your weekly budget; "))
transport_total = transport_cost * campus_days  
feeding_total = feeding_cost * campus_days
total =  transport_total + feeding_total + other_expenses
print()
print("WEEKLY EXPENSE SUMMARY")
print("=========================")
print("Student:", name)
print(f"Transport total:NGN {transport_total:,.2f}")
print(f"Feeding total:NGN {feeding_total:,.2f}")
print(f"Other expenses:NGN {other_expenses:,.2f}")
print(f"Weekly total:NGN {total:,.2f}")
print()
if total > budget:
    print("weekly expense is above the budget!!!")
if total <= budget:
    print("weekly expense is within the budget!!!")
if total == budget:
    print("weekly budget is exactly the same as the budget!!!")
