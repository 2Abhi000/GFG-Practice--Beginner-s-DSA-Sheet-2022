#Reverse a linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
#efficient approach O(1)
def reversll(head):
    if head is None or head.next is None:
        return head
    sh=reversll(head.next)
    tail=head.next
    tail.next=head
    head.next=None
    return sh

def printLL(head):
    while(head is not None):
        print(str(head.data) + "->",end='')
        head=head.next
    print("None")
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
head=reversll(head)
printLL(head)

