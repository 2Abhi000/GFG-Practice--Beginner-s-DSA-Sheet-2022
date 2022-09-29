#Number of 1 Bits
k=int(input())
bi=(str(bin(k))[2:])
c=0
for i in bi:
    if(i=='1'):
        c=c+1
print(c)
