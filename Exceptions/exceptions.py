try:
    with open("exceptions.py") as file, open("another.txt") as target:
        print("File opened")
    # age = int(input("Age: "))
    # xfactor = 10 / age
except (ValueError, ZeroDivisionError) as error:
    print("You didn't enter a valid age")
    print(error)
    print(type(error))
# except ZeroDivisionError:
#     print("Age cannot be zero")
else:
    print("No exceptions were thrown")
# if you use with statement, you don't need the finally clause
# finally:
#     file.close()

# raising errors is a costly style

from timeit import timeit

code1 = """

def calculateXfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    calculateXfactor(-1)
except ValueError as error:
    pass

"""
code2 = """

def calculateXfactor(age):
    if age <= 0:
        None
    return 10 / age

xfactor = calculateXfactor(-1)
if xfactor == None:
    pass

"""


print("First code", timeit(code1, number=10000))
print("Second code", timeit(code2, number=10000))
