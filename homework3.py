# 1. Find the big number
# accept input - a list of number '2,5,8,9,18'
# expected output - max number 18
"""awn = input("plz enter a list of numbers seperated by commas :       ")
n1 = awn.split(',')
mxnumb = 0
for item in n1:
    if int(item) > mxnumb:
        mxnumb = int(item)
print(mxnumb)"""

# 2. Sorting

# accept input - a list of numbers
# output - sorted list of numbers

# example: 
# input - 5, 2, 4, 3, 8
# output - 2, 3, 4, 5, 8
a = input("plz enter mixed numbers seperated by commas :    ")
b = a.split(',')
min1 = 0
item2 = 0
result = []
while len(b) > 0:
    min1 = b[0]

    for item2 in b:
        if int(min1) > int(item2):
            min1 = item2

    result.append(min1)
    b.remove(min1)
print(result)