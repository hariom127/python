# What is Operators: In simple words, operators are special symbols or keywords used to perform operations on values/variables.
# Operators in Python:
# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Assignment Operators
# 4. Logical Operators
# 5. Bitwise Operators
# 6. Identity Operators
# 7. Membership Operators


# Arithmetic Operators: These operators are used to perform mathematical operations like addition, subtraction, multiplication, division, etc.
print(2+2)  # Addition
print(2-2)  # Subtraction
print(2*2)  # Multiplication
print(2/2)  # Division
print(2%2)  # Modulus
print(3**2) # Exponentiation 3^2 = 3*3
print(5//2) # Floor Division

# Comparison Operators: These operators are used to compare two values and return a boolean value (True or False).
print(2==2)  # Equal to
print(2!=2)  # Not equal to
print(2>2)   # Greater than
print(2<2)   # Less than
print(2>=2)  # Greater than or equal to
print(2<=2)  # Less than or equal to


# Assignment Operators: These operators are used to assign values to variables.
x = 5  # Assigning value 5 to variable x
x += 2  # x = x + 2, OP: 7
x -= 2  # x = x - 2, OP: 5
x *= 2  # x = x * 2, OP: 10
x /= 2  # x = x / 2, OP: 5.0
x %= 2  # x = x % 2, OP: 1


# Logical Operators: These operators are used to combine conditional statements and return a boolean value (True or False).
a = True
b = False
print(a and b)  # Logical AND, OP: False
print(a or b)   # Logical OR, OP: True
print(not a)    # Logical NOT, OP: False


# Bitwise Operators: These operators are used to perform bit-level operations on binary numbers.
x = 5  # Binary: 0101
y = 3  # Binary: 0011
print(x & y)  # Bitwise AND, OP: 1 (Binary: 0001)
print(x | y)  # Bitwise OR, OP: 7 (Binary: 0111)
print(x ^ y)  # Bitwise XOR, OP: 6 (Binary: 0110)
print(~x)     # Bitwise NOT, OP: -6 (Binary: 1010)
print(x << 1) # Bitwise Left Shift, OP: 10 (Binary: 1010)
print(x >> 1) # Bitwise Right Shift, OP: 2 (Binary: 0010)


# Identity Operators: These operators are used to compare the memory locations of two objects.
x = 5
y = 5
print(x is y)  # Identity operator, OP: True (Both x and y point to the same memory location)
print(x is not y)  # Identity operator, OP: False


# Membership Operators: These operators are used to test if a value is present in a sequence (like a list, tuple, or string).
x = [1, 2, 3, 4, 5]
print(3 in x)  # Membership operator, OP: True (3 is present in the list x)
print(6 not in x)  # Membership operator, OP: True (6 is not present in the list x)

print("Hello" in "Hello World")  # Membership operator, OP: True (The substring "Hello" is present in the string "Hello World")
print("W" not in "Hello World")  # Membership operator, OP: False (The substring "World" is present in the string "Hello World")

