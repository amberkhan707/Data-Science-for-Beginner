# THIS IS MY FIRST PROGRAM
# program calculates simple interest

prin=0
rate=0
years=0
interest=0

print("Simple Interest Calculator")
prin= int(input("Enter Principal Value : "))
rate = float(input("Enter rate of interest : "))
years= float (input("Enter nubmer of years : "))

# calculate simple interest

interest = prin * rate * years / 100
maturity_amount = prin + interest

print()
print("Interst calculated is : " , interest)
print("Maturity Amount calculated is : " , maturity_amount)
print()

print("Job Done")



