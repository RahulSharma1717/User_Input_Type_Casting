#  Take the sides of a triangle and check whether it follows Pythagoras' theorem.
#       sq. of base + sq. of height = sq. of hypotenuse

base = int(input("Enter the base of triangle: "))
height = int(input("Enter the height of triangle: "))
hypotenuse = int(input("Enter the length of hypotenuse: "))

if base**2 + height**2 == hypotenuse**2:
    print("The triangle is Right Angled")
else:
    print("The triangle is not Right Angled")


"""OutputEnter the base of triangle: 9
Enter the height of triangle: 12
Enter the length of hypotenuse: 15
The triangle is Right Angled"""

