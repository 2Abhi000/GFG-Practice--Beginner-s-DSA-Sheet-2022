#rotate by 90 degree
def transpose_mat(mat):
    final=[]
    for i in range(len(mat)):
        k=[]
        for j in range(len(mat)):
            k.append(mat[j][i])
        final.append(k)
    for i in final[::-1]:
        print(i)
row= int(input("Size: "))
col= int(input("Size: "))
ma=[[int(input("Value: ")) for i in range(row)] for j in range(col)]
ans=transpose_mat(ma)
     
