"""In Python, loops are used to execute a block of code repeatedly based on a condition. The two main types of loops are for loops and while loops."""

# Examples are followed below :

""" (Type 1) For Loops : """

# Iterating over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry

# Using range to iterate a fixed number of times
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

""" (Type 2) While Loops : """

# Using a while loop to count down
count = 5
while count > 0:
    print(count)
    count -= 1

# Output:
# 5
# 4
# 3
# 2
# 1

""" (Type 3) Nested Loops : """

# Nested loop to print a multiplication table
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(i * j, end=' ')
    print()  # Newline after each row

# Output:
# 1 2 3 
# 2 4 6 
# 3 6 9 

""" (Type 4) Loop Control Statements : """

# Using break
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# Using continue
for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)

# Output:
# 0
# 1
# 3
# 4
