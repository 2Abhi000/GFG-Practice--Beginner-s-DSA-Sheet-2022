#Longest Increasing Subsequence
k=[]
def mapt(arr, index, subarr): 
    def issorted(ar):
        flag = 0
        if(all(ar[i] <= ar[i + 1] for i in range(len(ar)-1))):
            flag = 1
        if (flag) :
            return True
        else :
            return False
    if index == len(arr):
        if len(subarr) != 0:
            if issorted(subarr) and len(subarr)>=1:
                k.append(subarr)            
    else:
        mapt(arr, index + 1, subarr)
        mapt(arr, index + 1, subarr+[arr[index]])
re={}
n=int(input())
a=[]
for i in range(n):
    a.append(int(input("Enter the value: ")))
ans=mapt(a,0,[])
for i in k:
    re[len(i)]=i

if(len(re)!=0):
    final_ans=max(re)
    print(final_ans)
else:
    print(0)
