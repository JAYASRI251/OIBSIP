print ('=== BMI Calculator ===')
name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))

if weight <= 0 or height <= 0:
    print("Please enter a valid height and weight: ")
else:
    bmi = weight / (height * height)
    
    print("\nHello,", name)
    print("your BMI is:", round(bmi, 2))
    
    if bmi < 18.5:
        print("BMI category: Underweight")
    elif bmi < 25:
        print("BMI category: Normal range")
    elif bmi < 30:
        print("BMI category: Overweight")
    else:
        print("BMI category: Obesity range")
        