#Tower Of Hanoi
c=0
def toh(n,rod1,rod2,rod3):
    global c
    if(n==1):
        print("Moved 1st disk from",rod1,"to",rod3)
        c=c+1
        return
    toh(n-1,rod1,rod3,rod2)
    print("Moved",n, "disk from",rod1,"to",rod3)
    c=c+1
    toh(n-1,rod2,rod1,rod3)

n=int(input("Enter value: "))
x=toh(n,"a","b","c")
print(c)