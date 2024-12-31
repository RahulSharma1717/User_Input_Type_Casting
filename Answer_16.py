# Take the radius and height of a cylinder and calculate the total surface area.
#   total_surface_area= 2*3.14* radius *height + 2* 3.14 * sq. of radius

import math

radius = float(input("Enter the radius for cylinder: "))
height = float(input("Enter the height of cylinder: "))

pi = math.pi
total_surface_area = 2*pi*radius*(height + radius)
print()
print(f"Total Surface Area of the cylinder of radius {radius} and height {height} is {total_surface_area:.2f}")


"""Output:
Enter the radius for cylinder: 8.24
Enter the height of cylinder: 14.57

Total Surface Area of the cylinder of radius 8.24 and height 14.57 is 1180.95"""