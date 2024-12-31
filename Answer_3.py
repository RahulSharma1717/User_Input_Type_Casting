# Take Weight and height from the user and Calculate BMI.​

weight_kgs = float(input("Enter weight in kgs: "))
height_cms = float(input("Enter height in cms: "))
bmi = (weight_kgs/height_cms**2)*10000
print("Your BMI is ", bmi)


"""Output:
Enter weight in kgs: 97
Enter height in cms: 183
Your BMI is  28.96473468900236
"""