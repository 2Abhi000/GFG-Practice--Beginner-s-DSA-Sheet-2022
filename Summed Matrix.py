#Summed Matrix
#bruteforce approach time complexity O(n^2)
def summed(mat,query):
    c=0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]==query:
                c=c+1
    print(c)
#optimised approach O(1)
def summed2(mat,query):
    d={}
    c=0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] in d:
                d[mat[i][j]]+=1
            else:
                d[mat[i][j]]=1
    print(d[query])
row=int(input("Row: "))
col=int(input("Col: "))
ma=[[int(i+j) for i in range(1,row+1)] for j in range(1,col+1)]
q=int(input("Enter query: "))
ans=summed(ma,q)
ans=summed2(ma,q)
