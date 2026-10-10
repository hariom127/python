# How to create strings in Python

# Using single quotes
str1 = 'Hello, World!'

# Using double quotes
str2 = "Hello, World!"
str3 = "It's a beautiful day!"

# Using triple quotes for multi-line strings
str4 = """This is a
multi-line string."""


# Using the str() constructor
str5 = str("Hello, World!")


print(str1)
print(str2)
print(str3)
print(str4)
print(str5)


# Positive indexing
str6 = "Python"
print(str6[0])  # Output: P
print(str6[1])  # Output: y
print(str6[2])  # Output: t


# Negative indexing
print(str6[-1])  # Output: n
print(str6[-2])  # Output: o
print(str6[-3])  # Output: h

# Slicing
print(str6[0:2])  # Output: Py, Last index is not included
print(str6[2:4])  # Output: th
print(str6[:4])   # Output: Pyth
print(str6[0:5:2])   # Output: Pto, Step size is 2
print(str6[::-1])   # Output: nohtyP, Step size is -1, using for reversing the string

# String are immutable
str = "Hello"
# str[0] = 'h'  # This will raise an error because strings are immutable
print(str)  # Output: Hello