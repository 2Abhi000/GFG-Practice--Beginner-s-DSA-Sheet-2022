#Find minimum and maximum element in an array
n=int(input("Size: "))
a=[]
for i in range(n):
    a.append(int(input("Value: ")))
print(min(a),max(a))
