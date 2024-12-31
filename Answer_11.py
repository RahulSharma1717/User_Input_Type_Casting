#     Take 5 numbers from the user and calculate average of those numbers.

user_input = input("Enter numbers separated by spaces: ")
my_list = list(map(int, user_input.split()))

print("List of integers:", my_list)

sum = 0
for n in my_list:
    sum = sum + n

average = sum / len(my_list)
print(f"The average is: {average:.3f}")


"""Output:
Enter numbers separated by spaces: 56 38 94 61 58 74 12 34 51 66 80 98
List of integers: [56, 38, 94, 61, 58, 74, 12, 34, 51, 66, 80, 98]
The average is: 60.167"""