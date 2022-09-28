#print first n fibonacci numbers
n=int(input("No.: "))
n1, n2 =1, 1
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print(n1)
else:
   while count < n:
       print(n1,end=' ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1


