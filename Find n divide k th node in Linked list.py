#Find n/k th node in Linked list
from math import ceil
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printinode(head,node):
    k=[]
    c=0
    while(head is not None):
        c=c+1
        k.append(head.data)
        head=head.next
    print(k[ceil(len(k)/node)-1])
    return


#optmised aproach time colplexity=n 
def takeinp():
    inputt=[int(ele) for ele in input("Enter nodes space separated: ").split()]
    head=None
    tail=None
    for currdata in inputt:
        if currdata == -1:
            break

        newNode=Node(currdata)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head

head=takeinp()
no=int(input("Node: "))
printinode(head,no)
