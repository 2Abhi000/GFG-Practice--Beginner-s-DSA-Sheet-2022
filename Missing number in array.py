#Missing number in array
def se(a):
    for i in range(1,len(a)+1):
        if i not in a:
            print(i)
n=int(input("Size: "))
ar=[]
for i in range(n-1):
    ar.append(int(input("Value: ")))
ans=se(ar)
