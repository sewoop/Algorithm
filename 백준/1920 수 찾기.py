'''
n = int(input())
standard = list(map(int, input().split()))

m = int(input())
comparison = list(map(int, input().split()))

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = BinarySearchTreeNode(data)
        if self.root == None:
            self.root = newNode
            return

        node = self.root

        while True:
            preNode = node
            if node.data > newNode.data:
                node = node.left
                if node == None:
                    node = newNode
                    preNode.left = node
            elif node.data < newNode.data:
                node = node.right
                if node == None:
                    node = newNode
                    preNode.right = node
            else:
                return
                
    def search(self, data):
        node = self.root

        while True:
            if node.data > data:
                node = node.left
                if node == None:
                    print('0')
                    break
            elif node.data < data:
                node = node.right
                if node == None:
                    print('0')
                    break
            elif node.data == data:
                print('1')
                break
            else:
                print('0')
                break

bst = BinarySearchTree()
for data in standard:
    bst.insert(data)

for comp in comparison:
    bst.search(comp)
'''

n = int(input())
standard = set(map(int, input().split()))

m = int(input())
comparison = list(map(int, input().split()))

for comp in comparison:
    if comp in standard:
        print('1')
    else:
        print('0')
