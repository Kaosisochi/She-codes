# quantity = 3
# itemno = 567
# price = 49.95

# txt = "i want {0} quantities of deio and {2} items of mio with a price of {1}"
# print (txt.format(quantity, itemno, price))


# thislist=["apple","banana","cherry"]
# print(thislist[-1])


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)


# write a python program to check if the first number and the last number are thesame
# numbers_x = [10, 20, 30, 40, 10]
# Note:print good if it is thesame else print bad if it isn't

# numbers_x = [10, 20, 30, 40, 10]
# if numbers_x[0]==numbers_x[-1]:
#    print("good")
# else:
#    print("bad")


#print("Program to reverse a string")
# x = "1234abcd"
# print(x.reverse(x))


# program to calculate simple and compound interest
P = 35
R = 60
T = 4
print('For Simple Interest')
Simple_Interest = P*R*T
print(Simple_Interest)

print('For Compound Interest')
A = P*(1+(R/100))**T
Compound_Interest = A - P
print(Compound_Interest)

