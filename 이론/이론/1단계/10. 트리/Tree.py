## 이진 트리 (Binary tree)
### 이진 트리의 순회는 재귀 호출을 사용한다. 따라서 전위, 중위, 후위 순회를 간단하게 구현할 수 있다. 순회란 모든 원소를 빠트리거나 중복하지 않고 처리하는 연산을 의미한다.

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None

    # pre-oreder
    def preOrderTraversal(self, node: BinaryTreeNode):
        print(node, end='')
        if not node.left == None : self.preOrderTraversal(node.left)
        if not node.right == None : self.preOrderTraversal(node.right)

    # in-order
    def inOrderTraversal(self, node: BinaryTreeNode):
        if not node.left == None : self.inOrderTraversal(node.left)
        print(node, end='')
        if not node.right == None : self.inOrderTraversal(node.right)

    # post-order
    def postOrderTraversal(self, node: BinaryTreeNode):
        if not node.left == None : self.postOrderTraversal(node.left)
        if not node.right == None : self.postOrderTraversal(node.right)
        print(node, end='')

    def makeRoot(self, node: BinaryTreeNode, leftNode: BinaryTreeNode, rightNode: BinaryTreeNode):
        if self.root == None:
            self.root = node
        node.left = leftNode
        node.right = rightNode

# if __name__ == "__main__":
#     node = []
#     node.append(BinaryTreeNode(1))
#     node.append(BinaryTreeNode(2))
#     node.append(BinaryTreeNode(3))
#     node.append(BinaryTreeNode(4))
#     node.append(BinaryTreeNode(5))
#     node.append(BinaryTreeNode(6))
#     node.append(BinaryTreeNode(7))

#     m_tree = BinaryTree()
#     for i in range(int(len(node)/2)):
#         m_tree.makeRoot(node[i],node[i*2+1],node[i*2+2])

#     m_tree.preOrderTraversal(m_tree.root)
#     m_tree.inOrderTraversal(m_tree.root)
#     m_tree.postOrderTraversal(m_tree.root)


## 스레드 이진 트리 (Thread binary tree)
### 이진 트리의 위 특징 때문에 시스템 혹은 외부 스택을 관리해야하며 하위 레벨로 내려갈수록 재귀 호출의 깊이가 깊어져 비효율적일 수 있다. 스레드 이진 트리는 재귀 호출 없이 순회할 수 있도록 구현된 트리이다.

class ThreadBinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.is_thread_right = None

    def __str__(self):
        return str(self.data)

class ThreadBinaryTree:
    def __init__(self):
        self.root = None

    def inOrderTraversal(self, node):
        while not node.left == None:
            node = node.left
        print(node, end='')
        while True:
            node = self.findThread(node)
            print(node, end='')
            if node.right == None:
                break

    def findThread(self, node):
        pre_node = node
        node = node.right
        if node == None:
            return node
        if pre_node.is_thread_right:
            return node
        while not node.left == None:
            node = node.left
        return node

    def makeRoot(self, node, left_node, right_node, thread):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node
        node.is_thread_right = thread

# if __name__ == "__main__":
#     node = []
#     node.append(ThreadBinaryTreeNode('-'))
#     node.append(ThreadBinaryTreeNode('*'))
#     node.append(ThreadBinaryTreeNode('/'))
#     node.append(ThreadBinaryTreeNode('A'))
#     node.append(ThreadBinaryTreeNode('B'))
#     node.append(ThreadBinaryTreeNode('C'))
#     node.append(ThreadBinaryTreeNode('D'))

#     m_tree = ThreadBinaryTree()
#     for i in range(int(len(node)/2)):
#         m_tree.makeRoot(node[i],node[i*2+1],node[i*2+2], False)

#     m_tree.makeRoot(node[3], None, None, True)
#     m_tree.makeRoot(node[4], None, None, True)
#     m_tree.makeRoot(node[5], None, None, True)

#     node[3].right = node[1]
#     node[4].right = node[0]
#     node[5].right = node[2]

#     print('중위 순회 : ', end='') ; m_tree.inOrderTraversal(m_tree.root)



## 이진 탐색 트리 (Binary search tree)
###  트리를 효율적으로 구현하고 사용하기 위해서 일정한 조건으로 정의한 것이다. 탐색용 자료구조로 사용되어 노드의 크기에 따라서 위치를 정의한다.
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertElement(self, data):
        newNode = BinarySearchTreeNode(data)
        if self.root == None:
            self.root = newNode
            return

        node = self.root
        while True:
            preNode = node # 이전 노드 저장
            if node.data > newNode.data: # 새 노드의 데이터가 기존 노드보다 작으면
                node = node.left # 왼쪽 노드로 이동
                if node == None: # 이동 후의 노드가 빈 노드이면 새 노드를 달아줌
                    node = newNode
                    preNode.left = node
            elif node.data < newNode.data: # 새 노드의 데이터가 기존 노드보다 크면
                node = node.right # 오른쪽 노드로 이동
                if node == None: # 이동 후의 노드가 빈 노드이면 새 노드를 달아줌
                    node = newNode
                    preNode.right = node
            else: return # 값이 기존 노드와 똑같으면 취소

    def __insertValue(self, node: BinarySearchTreeNode, data):
        if node is None:
            node = BinarySearchTreeNode(data)
        else:
            if data <= node.data:
                node.left = self.__insertValue(node.left, data)
            else:
                node.right = self.__insertValue(node.right, data)
        return node

    def insertElementV2(self, data):
        self.root = self.__insertValue(self.root, data)
        return self.root is not None

    def searchElement(self, data):
        node = self.root
        while True:
            if node.data > data:
                node = node.left
            elif node.data < data:
                node = node.right
            elif node.data == data:
                break
            else:
                return BinarySearchTreeNode('결과 없음')
        return node
    
    def __searchValue(self, root: BinarySearchTreeNode, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self.__searchValue(root.left, key)
        else:
            return self.__searchValue(root.right, key)

    def searchElementV2(self, key):
        return self.__searchValue(self.root, key)

    def __deleteValue(self, node: BinarySearchTreeNode, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right: # two child
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right: # one child
                node = node.left or node.right
            else: # no child
                node = None
        elif key < node.data:
            node.left, deleted = self.__deleteValue(node.left, key)
        else:
            node.right, deleted = self.__deleteValue(node.right, key)
        return node, deleted

    def deleteElementV2(self, key):
        self.root, deleted = self.__deleteValue(self.root, key)
        return deleted
    
    def preOrderTraversal(self, node: BinarySearchTreeNode):
        print(node, end=' ')
        if not node.left == None : self.preOrderTraversal(node.left)
        if not node.right == None : self.preOrderTraversal(node.right)

    def inOrderTraversal(self, node: BinarySearchTreeNode):
        if not node.left == None : self.inOrderTraversal(node.left)
        print(node, end=' ')
        if not node.right == None : self.inOrderTraversal(node.right)
    
    def postOrderTraversal(self, node: BinarySearchTreeNode):
        if not node.left == None : self.postOrderTraversal(node.left)
        if not node.right == None : self.postOrderTraversal(node.right)
        print(node, end=' ')

import random

if __name__ == "__main__":
    tree = BinarySearchTree()

    tree.insertElement(10)
    for i in range(20):
        tree.insertElement(i)

    print("전위 순회: ")
    tree.preOrderTraversal(tree.root)
    print()

    print("중위 순회: ")
    tree.inOrderTraversal(tree.root)
    print()

    print("후위 순회: ")
    tree.postOrderTraversal(tree.root)
    print()

    print(tree.deleteElementV2(5))

    print("전위 순회: ")
    tree.preOrderTraversal(tree.root)
    print()

    print("중위 순회: ")
    tree.inOrderTraversal(tree.root)
    print()

    print("후위 순회: ")
    tree.postOrderTraversal(tree.root)
    print()

    print(tree.searchElementV2(5))



## AVL트리 (AVL tree)
### 이진 탐색 트리는 좌우 균형이 잘 맞으면 탐색 성능이 높다. AVL 트리는 각 노드의 왼쪽 서브 트리의 높이와 오른쪽 서브 트리의 높이를 비교하여 트리의 균형을 조절한다.






## 힙 (Heap): 최대힙, 최소힙
### 노드중에서 키값이 가장 큰 노드나 가장 작은 노드를 찾기 위해 만든 자료구조다.






