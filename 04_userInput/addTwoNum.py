firstNum = input("Enter first number: ")
secondNum = input("Enter second number: ")

# Convert the input strings to integers
firstNum = int(firstNum)
secondNum = int(secondNum)

# Calculate the sum of the two numbers
sum = firstNum + secondNum

# Display the result
print("The sum of", firstNum, "and", secondNum, "is:", sum)

# Implicit type vs Explicit type conversion
# Implicit type conversion (type casting) is when Python automatically converts one data type to another
firstNum = 5 # integer
secondNum = 2.5 # float

# Implicit type conversion: Python automatically converts the integer to a float
result = firstNum + secondNum # result will be a float
print("The implicit result", result)

# Explicit type conversion (type casting) is when the programmer manually converts one data type to another
firstNum = 5 # integer
secondNum = 2.5 # float

# Explicit type conversion: the programmer manually converts the float to an integer
result = firstNum + int(secondNum) # result will be an integer
print("The explicit result", result)