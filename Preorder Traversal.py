#Preorder Traversal
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printPreorder(root):
 
    if root:
        print(root.val,end=' ')
        printPreorder(root.left)
        printPreorder(root.right)
 
 
if __name__ == "__main__":
  root = Node(6)
  root.left = Node(3)
  root.right = Node(2)
  root.left.left = Node(1)
  root.right.right = Node(2)
  printPreorder(root)
