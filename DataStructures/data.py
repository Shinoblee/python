from pprint import pprint
from sys import getsizeof
from array import array
from collections import deque

letters = ["a", "b", "c", "d"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
# print(combined)
# numbers = list(range(20))
chars = list("Hello World")
# print(len(chars))
# letters[0] = "A"
# print(numbers[::-1])

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

numbers = [1, 2, 3, 4, 4, 4, 5, 6, 9]
# This is list unpacking / Can only be used if you match #of variables with length of list
# first, second, third = numbers

# Can have wildcard that will store rest of items in separate list
first, second, *other, last = numbers

# items = [0, "a"]
# index, letter = items

# for index, letter in enumerate(letters):
#     print(index, letter)

# Add
# append will add at the end
letters.append("e")
# insert will do at position
letters.insert(3, '-')

# Remove
# letters.pop(3)
# letters.remove("-")
# del letters[0:3]
# letters.clear()

# print(letters.count("f"))

# if "d" in letters:
#     print(letters.index("d"))

# randomNumbers = [3, 51, 2, 8, 6]
# randomNumbers.sort(reverse=True)
# This will not change the original list
# sorted(randomNumbers)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


# def sortItems(item):
#     return item[1]


# items.sort(key=lambda item: item[1])

# prices = []
# for item in items:
#     prices.append(item[1])

# prices = list(map(lambda item: item[1], items))
# print(prices)
# list comprehension
# [expression for item in items]
# Same as line 68
prices = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] >= 10, items))
# Same as line 75
filtered = [item for item in items if item[1] >= 10]

list1 = [1, 2, 3]
list2 = [10, 20, 30]

# [(1, 10), (2, 20), (3, 30)]
# print(list(zip("abc", list1, list2)))

# browsingSession = []
# browsingSession.append(1)
# browsingSession.append(2)
# browsingSession.append(3)
# print(browsingSession)
# last = browsingSession.pop()
# print(last)
# print(browsingSession)
# print("redirect", browsingSession[1])
# if not browsingSession:
#     print("disabled")

# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)

# queue.popleft()
# print(queue)
# if not queue:
#     print("empty")


# tuples is a read only list
point = (1, 2, 3)
# point = tuple([1, 2])
# print(point[1])
# x, y, z = point
if 10 in point:
    print("exists")


x = 10
y = 11

x, y = y, x
a, b = 1, 2

# numbers = array('i', [1, 2, 3])
# numbers.append(4)

numbers = [1, 1, 2, 3, 4]
second = {1, 5}
first = set(numbers)

# This is a union of sets
# print(first | second)
# # This is an intersection of sets
# print(first & second)
# # This is the difference between the two lists
# print(first - second)
# # This is the semetric difference / will return items in either first or second but not both
# print(first ^ second)

point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
# print(point.get("a", 0))
del point["x"]
# print(point)
# for key, value in point.items():
#     print(key, value)

# values = []
# for x in range(5):
#     values.append(x*2)

# Dictionary comprehension
# values = {x: x * 2 for x in range(5)}
# print(values)

# if you have a very large dataset, use a generator expression to save on memory considerations
values = (x * 2 for x in range(100000))
# print("gen: ", getsizeof(values))


values = list(range(5))
values = [*range(5), *"Hello"]

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}


sentence = "This is a common interview question"

charFrequency = {}
for char in sentence:
    if char in charFrequency:
        charFrequency[char] += 1
    else:
        charFrequency[char] = 1

charFrequencySorted = (
    sorted(charFrequency.items(),
           key=lambda kv: kv[1],
           reverse=True))
print(charFrequencySorted[0])
