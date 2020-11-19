emp_name = input("your name pls  :" . strip ().title())
hourly_wage = int(input("your hourly wage  :" ))
total_hours_worked = int(input("number of hours : "))
total_wage = total_hours_worked * hourly_wage
print(f"{emp_name} earned {total_wage}$ this week")
