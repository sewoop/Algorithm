from typing import Union

class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = self.right = None

class BSTree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    def insert(self, data: int) -> None:
        new_node = Node(data)
        curr = self.__root
        prev = self.__root

        if not self.__root:
            self.__root = new_node
            return

        while curr:
            if curr.data > data:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right

        if prev.data > data:
            prev.left = new_node
        else:
            prev.right = new_node
    
    def search(self, data: int) -> Union[Node, None]:
        curr = self.__root
        while curr:
            if curr.data == data:
                return curr
            elif curr.data > data:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def delete(self, data: int) -> bool:
        if self.__root == None:
            return False
        else:
            curr = self.__root
            prev = self.__root
            check = False

            # Checking
            while curr:
                if curr.data == data:
                    check = True
                    break
                elif curr.data > data:
                    prev = curr
                    curr = curr.left
                else:
                    prev = curr
                    curr = curr.right

            if not check:
                return False

            # Case 1. No child
            if curr.left == None and curr.right == None:
                if curr.data > data:
                    prev.left = None
                else:
                    prev.right = None
        
            # Case 2. one child
            elif curr.left != None and curr.right == None:
                if curr.data > data:
                    prev.left = curr.left
                else:
                    prev.right = curr.left

            elif curr.left == None and curr.right != None:
                if curr.data > data:
                    prev.left = curr.right
                else:
                    prev.right = curr.right

            # Case 3. two child
            else:
                if curr.data > data:
                    change_node = curr.right
                    change_node_prev = curr.right

                    while curr.left:
                        change_node_prev = change_node
                        change_node = change_node.left
                    
                    if change_node.right:
                        change_node_prev.left = change_node.right
                    else:
                        change_node_prev.left = None
                    
                    prev.left = change_node
                    change_node.right = curr.right
                    change_node.left = curr.left

                else:
                    change_node = curr.right
                    change_node_prev = curr.right
                    while change_node.left != None:
                        change_node_prev = change_node
                        change_node = change_node.left

                    if change_node.right != None:
                        change_node_prev.left = change_node.right
                    else:
                        change_node_prev.left = None
                    
                    prev.right = change_node
                    change_node.left = curr.left
                    change_node.right = curr.right
                    
            return True

    def delete_recur(self, curr: Node, data: int) -> Union[Node, None]:
        if not curr:
            return None
        elif curr.data > data:
            curr.left = self.delete_recur(curr.left, data)

        elif curr.data < data:
            curr.right = self.delete_recur(curr.right, data)
        
        else:
            # Case 1. No child
            if not curr.left and not curr.right:
                curr = None
            
            # Case 2. one child
            elif not curr.left:
                curr = curr.right
            elif not curr.right:
                curr = curr.left
            
            # Case 3. two child
            else:
                rep = curr.left

                while rep.right:
                    rep = rep.right

                    curr.data, rep.data = rep.data, curr.data

                    curr.left = self.delete_recur(curr.left, rep.data)
        return curr

    def pre_order_traversal(self):
        res = []
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                res.append(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.__root)

        print(res)

    def in_order_traversal(self):
        res = []
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                res.append(root.data)
                _in_order_traversal(root.right)
        _in_order_traversal(self.__root)

        print(res)

    def post_order_traversal(self):
        res = []
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                res.append(root.data)
        _post_order_traversal(self.__root)

        print(res)
        

class BST:
    def __init__(self) -> None:
        self.root = None

    def search(self, root: Node, data: int) -> Node:
        if root == None or root.data == data:
            return root
        if root.data > data:
            return self.search(root.left, data)
        if root.data < data:
            return self.search(root.right, data)

    def insert(self, data: int) -> None:
        def insert_(root: Node, data: int) -> Node:
            if root == None:
                root = Node(data)
                return root
            if root.data > data:
                root.left = insert_(root.left, data)
            elif root.data < data:
                root.right = insert_(root.right, data)
            return root

        self.root = insert_(self.root, data)

    def delete(self, data: int): 
        def delete_(root: Node, data: int) -> Node:
            if root == None:
                return root
            if root.data > data:
                root.left = delete_(root.left, data)
            elif root.data < data:
                root.right = delete_(root.right, data)
            else:
                if root.left == None and root.right == None:
                    return None
                elif root.left == None:
                    return root.right
                elif root.right == None:
                    return root.left
                
                root.data = find_min(root.right)
                root.right = delete_(root.right, root.data)
            return root

        def find_min(root: Node) -> int:
            min_ = root.data
            while root.left:
                min_ = root.left.data
                root = root.left

            return min_

        self.root = delete_(self.root, data)
    
    def pre_order(self):
        res = []
        def __pre_order_(root):
            if root is None:
                pass
            else:
                res.append(root.data)
                __pre_order_(root.left)
                __pre_order_(root.right)
        __pre_order_(self.root)

        print(res)

    def in_order(self):
        res = []
        def __in_order_(root):
            if root is None:
                pass
            else:
                __in_order_(root.left)
                res.append(root.data)
                __in_order_(root.right)
        __in_order_(self.root)

        print(res)

    def post_order(self):
        res = []
        def __post_order_(root):
            if root is None:
                pass
            else:
                __post_order_(root.left)
                __post_order_(root.right)
                res.append(root.data)
        __post_order_(self.root)

        print(res)

ts = int(input())

for t in range(1, ts + 1):
    N = int(input())

    tree = BST()
    
    # 1 2 3 4 5 6
    # 1 2 3 4 5 6 7 8
    tree.insert(4)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(6)
    tree.insert(5)

    tree.pre_order()
    tree.in_order()
    tree.post_order()

