#Count Palindrome Sub-Strings of a String
def printAllpalindromeSubstrings(s, n):
    ar=[]
    for i in range(n):
        temp=""
        for j in range(i,n):
            temp+=s[j]
            if temp==temp[::-1] and len(temp)>1:
                ar.append(temp)
    print(len(list(set(ar))))
            
s = input("Enter string: ")
printAllpalindromeSubstrings(s, len(s))