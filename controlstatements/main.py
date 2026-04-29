# what is control statements?
# control statements are used to control the flow of the program.
#  They are used to make decisions and to repeat a block of code.
# types of control statements
# 1. if statement
# 2. if-else statement
# 3. if-elif-else statement
# 4. nested if statement

# x=7
# y=7

# if x>y:
#     print("x is greater than y")
# elif x==y:
#     print("x is equal to y")
# else:
#     print("y is greater than x")

# WAP to enter any number and check whether it is even or odd.
# WAP to enter age and check whether the person is eligible to vote or not.
# WAP to enter five subjects marks and calculate the percentage and grade. (40-50=D, 50-60=C, 60-70=B, 70-80=A, 80-90=A+, 90-100=O)


# x=9
# y=6
# z=70

# if x>y:
#     if x>z:
#         print("x is the greatest number")
#     else:
#         print("z is the greatest number")
# else:
#     if y>z:
#         print("y is the greatest number")
#     else:
#         print("z is the greatest number")

# if x>y and x>z:
#     print("x is the greatest number")
# elif y>x and y>z:
#     print("y is the greatest number")
# else:
#     print("z is the greatest number")


# username = input("Enter your username: ")
# password = input("Enter your password: ")


# if username=="admin":
#     if password=="admin123":
#         print("Login successful")
#     else:
#         print("Invalid password")
# else:
#     print("Invalid username")
# if username=="admin" and password=="admin123":
#     print("Login successful")
# else:
#     print("Invalid username or password")

# language = "nepali"

# match language:
#     case "nepali":
#         print("Namaste")
#     case "english":
#         print("Hello")
#     case "hindi":
#         print("Namaste")
#     case _:
#         print("Language not supported")

# print(10/0)


# x=int(input("Enter first number: "))
# y=int(input("Enter second number: "))
# print("+,- , *, /")
# operator = input("Enter operator: ")

# match operator:
#     case "+":
#         print(x+y)
#     case "-":
#         print(x-y)
#     case "*":
#         print(x*y)
#     case "/":
#         if y!=0:
#             print(x/y)
#         else:
#             print("Cannot divide by zero")
#     case _:
#         print("Invalid operator")