#Inorder Traversal
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
 
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)
 
if __name__ == "__main__":
  root = Node(1)
  root.left = Node(3)
  root.right = Node(2)
  printInorder(root)
