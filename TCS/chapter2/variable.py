"""
• Rules for variable name in Python:
• Must start with a letter or the underscore character
• Cannot start with a number
• Can only contain alpha (az), numeric characters (0-9) and underscores ( _ )
• Don't use Python's keyword to name variables
• Case-sensitive (age, Age and AGE are three different variables)

Example:
• Correct variable name: Hello_1 _Hello
• Variables are different : spam Spam SPAM
• Incorrect variable name:
• 1_Hello: start with a number character
• He llo: contains spaces
• print: Python's keyword

Python không có lệnh để khai báo biến
Toán tử gán: =

Multiple data types can be assigned to a variable
• Variables can also specific to the particular data type with casting
x = 4
x = "Sally"
# x is of type int
# x is now of type str
x = str(3) # x will be '3'
y = int(3) # y will be 3

One values can be assigned to multiple variables
• Many values can be assigned to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
a = b = c = 1
• It is possible to query that data through the variable name
x = "Orange"
print(x)  Orange
• The input() function allows user input
x = input('Enter your name:')
print('Hello, ' + x)

Hằng số là một đại lượng có giá trị không đổi
"""

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)   
print(z)

a = b = c = 1
print(a)
print(b)
print(c)

x = input('Enter your name:')
print('Hello, ' + x)

