#Check whether K-th bit is set or not
def kbit(n,k):
    if(((n>>k)&1)!=0):
        return True
    else:
        return False
n=int(input("Value: "))
k=int(input("Value: "))
ans=kbit(n,k)
if ans:
    print("YES")
else:
    print("No")