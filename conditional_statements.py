
# CONDITIONAL STATEMENTS

num = int(input("Enter number: "))

# if statement
if num > 0:
    print("Positive number")

# if else
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# if elif else
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Nested if
age = int(input("Enter age: "))

if age >= 18:
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Adult")
else:
    print("Minor")