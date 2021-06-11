# String operation 2
awn = input("plz input a list,seperated by commas: ")
a = awn.split(',')
b = []
for i in range(len(a)):
    if int(a[i]) % 3 != 0:
        b.append(a[i])
c = ''
for i in range(len(b)):
    c = c + b[i] + ','
d = c[0:(len(c)-1)]
print(d)