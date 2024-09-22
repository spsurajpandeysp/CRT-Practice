

# a = 0
# b =10

# # print(b/a)


# try:
#     print(b/a)
# except ZeroDivisionError:
#     print("Not allowed divide by zero ")



# try:
#     print(b/a)
# except ZeroDivisionError as msg:
#     print(msg)


# try:
    
#     a = int(input("Enter number"))
#     b = int(input("Enter number"))
#     print(b/a)
# except ZeroDivisionError as msg:
#     print(msg)
# except ValueError as msg:
#     print(msg)



# try:
    
#     a = int(input("Enter number"))
#     b = int(input("Enter number"))
#     print(b/a)
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg)

a = 10
b = 0


try:
    print("try")
    print(a//b)
except ZeroDivisionError as msg:
    print(msg)

finally:
    print('finally')


try:
    print("try")
    print(a//b)
except NameError as msg:
    print(msg)

finally:
    print('finally')