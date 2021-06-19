#print pyramid

l = int(input("write a number:     "))
for i in range(l):
   for a in range(l-i+1):
       print(' ',end = '')
   for a in range(i*2-1):
       print('A',end = '')
   print(' ')

