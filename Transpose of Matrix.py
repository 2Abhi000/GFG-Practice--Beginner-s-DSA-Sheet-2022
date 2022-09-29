#Transpose of Matrix
def transpose_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[j][i],end=' ')
        print()
row= int(input("Size: "))
col= int(input("Size: "))
ma=[[int(input("Value: ")) for i in range(row)] for j in range(col)]
ans=transpose_mat(ma)
     
