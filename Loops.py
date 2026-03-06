
# LOOPS IN PYTHON

# for loop
for i in range(1, 6):
    print(i)

# while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# break example
for i in range(10):
    if i == 5:
        break
    print(i)

# continue example
for i in range(5):
    if i == 2:
        continue
    print(i)

# Sum of numbers
total = 0
for i in range(1, 6):
    total += i

print("Sum:", total)