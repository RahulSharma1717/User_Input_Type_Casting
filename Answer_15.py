# Take the length, breadth, and height of a cuboid in cm and calculate the volume of the cuboid.
#        volume= length * breadth * height

length = float(input('Enter length of the cuboid: '))
breadth =float(input('Enter breadth of the cuboid: '))
height = float(input('Enter height of the cuboid: '))

volume = length * breadth * height
print()
print(f'Volume of the cuboid is {volume:.3f} cubic cms')


"""Output:
Enter length of the cuboid: 56.32
Enter breadth of the cuboid: 74.12478
Enter height of the cuboid: 86.9546127893

Volume of the cuboid is 363010.084 cubic cms"""