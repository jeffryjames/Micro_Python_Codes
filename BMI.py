Height = float(input("Enter input in centimeters:"))
Weight = float(input("Enter weight:"))
Height = Height/100
BMI = Weight/Height*Height
print("Your BMI is",BMI)

if (BMI>=0):
    if (BMI<=16):
        print("Less Weight")
    elif(BMI<=18.5):
        print("Underweight")
    elif(BMI<=25):
        print("Healthy")
    elif(BMI<=30):
        print("Overweight")
    else: 
        print("Severely Overweight")
else: 
    print("Incorrect Input details ")