#Anagram
s=input("Enter first string: ")
s2=input("Enter another string: ")
def ana(x,y):
    s1=list(x)
    s2=list(y)
    if len(s1)==len(s2):
        return True
    else:
        return False
ans=ana(s,s2)
if(ans):
    print("YES")
else:
    print("NO")