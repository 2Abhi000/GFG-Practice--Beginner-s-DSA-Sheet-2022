#Wave Array
def wave(arr):
    arr.sort()
    for i in range(0,len(arr)-1,2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)
m=int(input("Size:"))
a=[]
for i in range(m):
    a.append(int(input("Value: ")))
ans=wave(a)
