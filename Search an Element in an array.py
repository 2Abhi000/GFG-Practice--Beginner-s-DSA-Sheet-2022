#Search an Element in an array
def findd(a,e):
    if e in a:
        print(a.index(e))
    else:
        print('not found')
n=int(input("Size: "))
ar=[]
for i in range(n):
    ar.append(int(input("Value: ")))
ele=int(input("element: "))
ans=findd(ar,ele)
