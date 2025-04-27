# Pay Calculation
# Program inputs the basic pay and the grade of the employee
# Input: Basic Pay , number
# Input Grade : grade 1, 2 or 3
# Pay calculation Rules
# Gross Pay = Basic Pay + DA + HRA - MT

# DA calculation:
# if grade = 1 DA = 10000
# if grade = 2 DA = 50% of basic
# if grade = 3 DA = 75% of basic

# HRA Calculation:
# if grade = 1 HRA = 12000
# if grade = 2 HRA = 40% of basic
# if grade = 3 HRA = 60% of basic

# MT (Monthly Tax) calculation:
# Monthly_Earning = Basic + DA + HRA
# If Monthly_Earning < 40000 , MT = 0
# If Monthly_ Earning > 40000, MT = 10% of Monthly_Earning

# Gross_Pay Calculations:
# Gross Pay = Basic Pay + DA + HRA - MT

# Ouptput:
# Earnings: Basic, DA, HRA, Monthly_Earning
# Deductions: MT
# Gross_Pay = Earnings - Deductions

# input data
print('Payroll Calculator')
basic = int(input("Enter basic pay: "))
grade = int(input("Enter Grade: "))

# Calculate DA
da=0
if grade == 1:
    da = 10000
else:
    if grade == 2:
        da = 0.5 * basic
    else:
        if grade == 3:
            da = 0.75 * basic


# Calculate HRA
# Calculate DA
hra=0
if grade == 1:
    hra = 12000
else:
    if grade == 2:
        hra = 0.4 * basic
    else:
        if grade == 3:
            hra = 0.6 * basic

# Calculate Monthly Earnings
earning=basic + da + hra

# Calculate monthly tax
if earning < 40000 :
    month_tax = 0
else:
    month_tax = 0.1 * earning

# calculate net pay
net_pay = earning - month_tax
print()
print("Pay Calculations")
print("Employee Grade: ", grade)
print("Employee Basic: ", basic)
print("Employee DA: ", da)
print("Employee HRA: ", hra)
print("Employee Earning: ", earning)
print("Employee Monthly Tax: ", month_tax)
print("Employee Net Pay: ", net_pay)
print()
print("Thanks")
