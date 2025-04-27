# BMI calculator

# This program calculate the BMI and reports if the person is normal or obese

weight=float(input("Please enter your weight (in kg) : "))
height = float(input ("input your height (mtr) :"))

# calcualte BMI

bmi = weight / (height * height)

print("Your BMI is :" , bmi)

if bmi <= 14.9 :
    print(" You are underweight")
    print('Eat well')
elif bmi < 25:
    print("Normal")
    print("Enjoy eating more")
elif bmi < 30:
    print("You ar over weight")
    print("Less Ice creams please")
else:
    print("You are Obese")
    print("Start fasting")

print("job done")


