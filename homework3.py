#sorting
a = input("plz enter mixed numbers seperated by commas :    ")
b = a.split(',')
min1 = 0
numb2 = 0
result = []
while len(b) > 0:
    min1 = b[0]

    for numb2 in b:
        if int(min1) > int(numb2):
            min1 = numb2

    result.append(min1)
    b.remove(min1)
print(result)