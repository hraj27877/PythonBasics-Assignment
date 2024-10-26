# Type-Casting : Type casting in Python is the process of converting a variable from one data type to another.

# Converting a String to an Integer :

num_str = "123"
num_int = int(num_str)  # Converts string to integer
print(num_int)           # Output: 123
print(type(num_int))     # Output: <class 'int'>

# Converting a Float to an Integer :

num_float = 12.75
num_int = int(num_float)  # Converts float to integer (truncates decimal)
print(num_int)             # Output: 12

# Converting an Integer to a String :

num = 456
num_str = str(num)        # Converts integer to string
print(num_str)            # Output: '456'
print(type(num_str))      # Output: <class 'str'>

# Converting a List to a Tuple :

my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # Converts list to tuple
print(my_tuple)            # Output: (1, 2, 3)

# Converting a String to a List :

my_string = "hello"
my_list = list(my_string)  # Converts string to list of characters
print(my_list)             # Output: ['h', 'e', 'l', 'l', 'o']

# Converting a String Representation of a Float to a Float :

float_str = "3.14"
num_float = float(float_str)  # Converts string to float
print(num_float)               # Output: 3.14

