"""Conditional statements in Python allow you to execute certain blocks of code based on whether a specified condition is true or false. The most common conditional statements are if, elif, and else"""

# Examples are followed below :

# (Type 1) Simple if-else :

age = 18

if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

# (Type 2) Using elif :

temperature = 30

if temperature < 0:
    print("It's freezing!")
elif temperature < 20:
    print("It's cold.")
elif temperature < 30:
    print("It's warm.")
else:
    print("It's hot.")

# (Type 3) Nested if statements :

num = 15

if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("It's even.")
    else:
        print("It's odd.")
else:
    print("The number is non-positive.")

# (Type 4) Combining Conditions :

x = 10
y = 5

if x > 0 and y > 0:
    print("Both numbers are positive.")
elif x < 0 or y < 0:
    print("At least one number is negative.")
else:
    print("Both numbers are zero.")


