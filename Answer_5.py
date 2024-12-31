# Your task is to take name and age  and  location from user and print the following message  :
#
# Hello Everyone , I am xyz and i am xyz years old and i live in xyz.


name = input("Enter your name: ")
age = input("Enter your age: ")
location = input("Enter the place you live: ")
print()
print(f"Hello Everyone , I am {name} and i am {age} years old and i live in {location}")    # I have used f-string interpolation here as placing commas and breaking the string thrice would have been tedious.


"""Output:
Enter your name: Rahul
Enter your age: 36
Enter the place you live: Bangalore

Hello Everyone , I am Rahul and i am 36 years old and i live in Bangalore"""