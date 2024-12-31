# Take the radius and length of a cone and calculate the total surface area of it.
#   total_surface_area= 3.14*radius*(radius + length)

import math

radius = float(input('Enter radius of the cone: '))
length = float(input('Enter length of the cone: '))
pi = math.pi

total_surface_area = pi * radius * (radius + length)
print(f'Total surface area of the cone with radius {radius} and length of side {length} is {total_surface_area:.3f}')


"""Output:
Enter radius of the cone: 23.697
Enter length of the cone: 79.354
Total surface area of the cone with radius 23.697 and length of side 79.354 is 7671.768"""