# Suppose there are many N numbers of people in the Army. We need to distribute them in G groups. Take the number of people from users and the Number of Groups and tell how many are left without Group.

N = int(input("Enter no. of Army people: "))
G = int(input("Enter no. of groups you want them to be distributed: "))
left_outs = N % G
print("The number of people left out after group formation:", left_outs)


"""Output:
Enter no. of Army people: 500
Enter no. of groups you want them to be distributed: 40
The number of people left out after group formation: 20"""