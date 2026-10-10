# print("Hello" + " World!")  # Concatenation of strings

# print("Hello" * 3)  # Repetition of strings
# # OP: HelloHelloHello

# print("Delhi" in "Delhi is the capital of India")  # Membership operator
# # OP: True

# print("Delhi" not in "Delhi is the capital of India")  # Membership operator
# # OP: False

# print("Delhi" == "Delhi")  # Comparison operator
# # OP: True

# print("Delhi" != "Mumbai")  # Comparison operator
# # OP: True

# print("Delhi" > "Mumbai")  # Comparison operator
# # OP: False
# # Explanation: In Python, string comparison is done lexicographically using the Unicode values of the characters. Since 'D' comes before 'M' in the Unicode table, "Delhi" is considered less than "Mumbai".

# print("Pune" > "pune")  # Comparison operator
# # OP: False
# # Explanation: In Python, string comparison is done lexicographically using the Unicode values of the characters. Since 'P' comes before 'p' in the Unicode table, "Pune" is considered less than "pune".


str = "Hello" and "World"
print(str)  # Output: World
# Explanation: The 'and' operator returns the second operand if the first operand is truthy. Since "Hello" is a non-empty string (which is considered truthy), the result of the expression is "World".

str = "Hello" or "World"
print(str)  # Output: Hello
# Explanation: The 'or' operator returns the first operand if it is truthy. Since "Hello" is a non-empty string (which is considered truthy), the result of the expression is "Hello".

