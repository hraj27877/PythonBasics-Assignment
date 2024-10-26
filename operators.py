#  Operators : It is responsible for any action carried over operants.

# According to there use cases there are different type of operators with are as follows:-

# (Type 1) Arithematic Operators:

a = 10
b = 3

print(a + b)  # For Addition Output: 13
print(a - b)  # For Substraction Output: 7
print(a * b)  # For multiplication Output: 30
print(a / b)  # For division Output: 3.3333...
print(a // b) # For remainder Output: 3
print(a % b)  # For modulus Output: 1
print(a ** b) # For exponential Output: 1000

# (Type 2) Compraision Operators:

x = 5
y = 10

print(x == y)  # For Equals to Output: False
print(x != y)  # For Not Equals to Output: True
print(x > y)   # For Greater than Output: False
print(x < y)   # For Smaller than  Output: True
print(x >= y)  # For Greater than Equals to Output: False
print(x <= y)  # For Smaller than Equals to Output: True

# (Type 3) Logical Operators: (And, Or, Not )

a = True
b = False

print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False

# (Type 4) Bitwise Operators:

a = 5  # (binary: 0101)
b = 3  # (binary: 0011)

print(a & b)  # Output: 1  (binary: 0001)
print(a | b)  # Output: 7  (binary: 0111)
print(a ^ b)  # Output: 6  (binary: 0110)
print(~a)     # Output: -6 (inverts bits)
print(a << 1) # Output: 10 (binary: 1010)
print(a >> 1) # Output: 2  (binary: 0010)

# (Type 5) Assignment Operators:

x = 5
x += 3  # Equivalent to x = x + 3
print(x)  # Output: 8

x *= 2  # Equivalent to x = x * 2
print(x)  # Output: 16

# (Type 6) Identity Operators:

a = [1, 2, 3]
b = a
c = list(a)

print(a is b)      # Output: True
print(a is c)      # Output: False
print(a == c)      # Output: True

# (Type 7) Membership Operators:

list = [1, 2, 3, 4, 5]

print(3 in list)      # Output: True
print(6 not in list)  # Output: True

