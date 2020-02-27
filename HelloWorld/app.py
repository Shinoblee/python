import math

print("Hello World")
print("*" * 10)

student_count = 1000
rating = 4.99
is_published = False
courseName = "Python Programming"
print(is_published)
print(len(courseName))
print(courseName[8])
print(courseName[-1])
print(courseName[0:3])
print(courseName[0:])
print(courseName[0:])
print(courseName[:3])

first = "Lee"
last = "Simon"
# This is an example of formatted strings
full = f"{first} {last}"
print(full)

print(courseName.upper())
print(courseName.lower())
print(courseName.title())
print(courseName.strip())
print(courseName.find("Pro"))
print(courseName.replace("P", "J"))
# Expression will return a boolean
print("swift" not in courseName)

#  a + bi <- complex numbers represented by a j
x = 1 + 2j

print(10 / 3)
# will remove the float
print(10 // 3)

x = 10
x += 3

print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2))

x = input("x: ")
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")

temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's Nice")
else:
    print("It's cold")

print("Done")

age = 12

message = "Eligible" if age >= 18 else "Not eligible"
print(message)

highIncome = False
goodCredit = True
student = False

if (highIncome or goodCredit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

# age should be between 18 and 65
age = 22

if 18 <= age < 65:
    print("Eligible")

# first two are range, finals is step
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
# will only work if the loop doesn't break out early
else:
    print("Attempted 3 times and failed")

for x in range(1, 6):
    for y in range(3):
        print(f"({x}, {y})")

print(type(5))
print(type(range(5)))

for x in [1, 2, 3, 4]:
    print(x)

number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command != "quit":
    command = input(">").lower()
    print("Echo", command)

while True:
    command = input(">")
    print("Echo", command)
    if command.lower() == "quit":
        break

counter = 0
for x in range(2, 9, 2):
    print(x)
    counter += 1
print(f"We have {counter} even numbers")
