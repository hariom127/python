# What is python?
# Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. It has a large standard library and a vibrant ecosystem of third-party packages, making it suitable for a wide range of applications, from web development to data science and artificial intelligence.


print("Hello, World!")

print(7)

print(3.14)

print("Python is fun!", 1, 3.7, True)
# OP: Python is fun! 1 3.7 True

print("Python is fun!", 1, 3.7, True, sep=" | ", end=" <END>\n") #sep: separator, end: what to print at the end
# OP: Python is fun! | 1 | 3.7 | True <END>


#end: default is \n, which means new line. If you want to change it, you can use end parameter.
print("Hello", end="-")
print("World")

# type function: returns the type of the object passed to it.
print(type(7)) # OP: <class 'int'>
print(type(3.14)) # OP: <class 'float'>
print(type("Hello, World!")) # OP: <class 'str'>


print("Data Science", "Mentorship", "Program", "By", "CampusX", sep="-") 
