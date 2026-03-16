
# Operators in Python

a = 10
b = 3

# Arithmetic Operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

principle = float(input("enter the principle amount : "))
rate = float(input("enter the annual intrest rate of(as a percentage): "))
time=float(input("enter the time in years: "))

# calculate the simple intrest

simple_intrest = (principle*rate*time)/100

print(f"the simple intrest is : {simple_intrest}")

## swapping two numbers using arithmatic operator

# a = 10
# b=20

# a,b=b,a
# print("a",a)
# print("b",b)

# #using arithmatic operation

# a= a+b
# b= a-b
# a= a-b

# print(f"a={a}, b={b}")

## find the avarage og three number

# num1= 10
# num2 = 20
# num3 =30 

# avarage= (num1+ num2+ num3)/3  # using basic arith matic
# print(avarage)

# import statistics
# numbers = [10, 20, 30]
# avarage= sum(numbers)/len(numbers)  # using len() and Sum()
# print(avarage)

# avarage= statistics.mean(numbers)  #using statistics mean()
# print(avarage)


# n = int(input("enter how many numbers to calculate avarage ? "))
# numbers = []

# for i in range(n):
#     num = float(input(f"{i+1}st Enter the number : "))
#     numbers.append(num)

# average = sum(numbers) / n
# print(f"Average is: {average}")


# Comparison Operators
print(a > b)
print(a < b)
print(a == b)
print(a != b)

# Logical Operators
x = True
y = False

print(x and y)
print(x or y)
print(not x)

# Assignment Operators
num = 5
num += 3
print(num)

# Identity Operators
print(a is b)
print(a is not b)

# Membership Operators
name = "Python"
print("P" in name)

print("z" not in name)

## Python Operators Practice Questions:

# 1.Write the to the sqaure of number using operator.

num= 6
print(num**2)

# 2.Write a program to check whether a number is between 10 and 20.
num=int(input("enter a Number: "))
if num>10 AND num <20:
Print("Number is Beetween 10 and 20")







