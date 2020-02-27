# def greet():
#     print("Hi there")
#     print("Welcome aboard")


# pep8 recommends two line breaks
# greet()

# def greet(name):
#     print(f"Hi {name}")


# def getGreeting(name):
#     return f"Hi {name}"


# message = getGreeting("Lee")
# file = open("content.txt", "w")
# file.write(message)

# optional parmaters have to be final parms
# def increment(number, by=1):
#     return number + by


# print(increment(2, 5))

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

# can pass key=value pairs
# def save_user(**user):
#     print(user["name"])


# save_user(id=1, name="Lee", age=37)

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start")
# print(multiply(1, 2, 3))


def fizzBuzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "Fizzbuzz"
    elif input % 5 == 0:
        return "Buzz"
    elif input % 3 == 0:
        return "Fizz"
    else:
        return input


print(fizzBuzz(15))
