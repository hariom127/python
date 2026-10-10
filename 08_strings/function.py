str = "Hello, world!"

print(len(str))  # Output: 13


print(str.upper())  # Output: HELLO, WORLD!

print(str.lower())  # Output: hello, world!

print(str.title())  # Output: Hello, World!

print(max(str))  # Output: w

print(min(str))  # Output: !


sorted_str = sorted(str)
print(sorted_str)  # Output:[' ', '!', ',', 'H', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r', 'w'] //ascending order of characters in the string

sorted_str = sorted(str, reverse=True)
print(sorted_str)  # Output:['w', 'r', 'o', 'o', 'l', 'l', 'l', 'e', 'd', 'H', ',', '!', ' '] //descending order of characters in the string

