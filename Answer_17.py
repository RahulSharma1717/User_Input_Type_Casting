#  Take the radius and height of a cone and calculate the volume of it.
#    volume= (3.14 * sq of radius * height) * 1/3

import math

radius = float(input('Enter radius of the cone: '))
height = float(input('Enter height of the cone: '))
pi = math.pi

volume = 1/3*(pi * radius**2 * height)
print(f'Volume of the cone with radius {radius} and height {height} is {volume:.3f}')


"""Output:
Enter radius of the cone: 5.25
Enter height of the cone: 7.88
Volume of the cone with radius 5.25 and height 7.88 is 227.443"""