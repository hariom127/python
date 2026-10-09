# variable is a container for storing data values
x = 5
y = "John"
print(x)
print(y)

# Dyanmic Typing: Python is dynamically-typed, which means you don't have to declare the type of a variable when you create one. The interpreter infers the type based on the value assigned to the variable.
x = 4       # x is of type int
x = "Sally" # x is now of type str

# Dynamic binding: In Python, variables are dynamically bound to objects. This means that a variable can be reassigned to different types of objects during its lifetime. For example, you can assign an integer to a variable and later reassign it to a string or a list.
x = 4
x = "Sally"
x = [1, 2, 3]

# Way of declaring multiple variables in one line
a, b, c = 1, 2, "John"

print(a, b, c)

a=b=c= 1
print(a, b, c)

