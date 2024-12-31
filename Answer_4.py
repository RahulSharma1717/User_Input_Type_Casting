# Take Principle, Rate, and Time From User and Calculate Simple Interest.

principal = int(input("Enter the Principal Amount: "))
rate_of_interest = float(input("Enter the annual rate of interest: "))
time_of_deposit = float(input("Enter the time of deposit in years: "))
simple_interest = principal * rate_of_interest * time_of_deposit / 100
print("Simple Interest on amount deposited", simple_interest)


"""Output:
Enter the Principal Amount: 10000
Enter the annual rate of interest: 6.5
Enter the time of deposit in years: 3.5
Simple Interest on amount deposited 2275.0"""