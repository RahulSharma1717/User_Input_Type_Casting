# Tom had y amount in his bank and jeff withdrew x amount where x is always less than y. Print the remaining balance in Tom's account. Take x and y from the user.

y = int(input("Guess amount in Tom's account: "))
x = int(input("What amount should Jeff withdraw: "))

if y > x:
    print("Remaining Balance in Tom's account:", y-x)
else:
    print("Please Jeff cannot withdraw an amount more than in Tom's account")


"""Output:
Guess amount in Tom's account: 1000
What amount should Jeff withdraw: 600
Remaining Balance in Tom's account: 400"""


"""Output:
Guess amount in Tom's account: 1000
What amount should Jeff withdraw: 1200
Please Jeff cannot withdraw an amount more than in Tom's account"""