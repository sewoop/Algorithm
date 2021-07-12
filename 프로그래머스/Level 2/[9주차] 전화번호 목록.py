''' 
# 효율성 시간초과
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr = self.head

        for char in string:
            if char not in curr.child:
                curr.child[char] = Node(char)
            curr = curr.child[char]
        curr.data = string

    def start_with(self, prefix):
        curr = self.head

        for pre in prefix:
            if pre in curr.child:
                curr = curr.child[pre]
            else:
                return None

        words = []
        curr = [curr]
        next_node = []

        while True:
            for node in curr:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.child.values()))
            if len(next_node) != 0:
                curr = next_node
                next_node = []
            else:
                break

        return words


def solution(phone_book):

    trie = Trie()

    for phone in phone_book:
        trie.insert(phone)

    for phone in phone_book:
        if len(trie.start_with(phone)) > 1:
            return False
    
    return True

# 효율성 시간초과
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr = self.head

        for char in string:
            if char not in curr.child:
                curr.child[char] = Node(char)
            curr = curr.child[char]
        curr.data = string

    def start_with(self, prefix):
        curr = self.head

        for pre in prefix:
            if pre in curr.child:
                curr = curr.child[pre]
            else:
                return False

        if curr.child:
            return True

        return False


def solution(phone_book):

    trie = Trie()

    for phone in phone_book:
        trie.insert(phone)

    for phone in phone_book:
        if trie.start_with(phone):
            return False
    
    return True

# 정렬을 이용하여 풀이 
# 효율성 3, 4번에서 시간 초과
def solution(phone_book):
    phone_book.sort()

    for i, phone1 in enumerate(phone_book):
        for phone2 in phone_book[i + 1:]:
            if phone2[:len(phone1)] == phone1:
                return False

    return True
'''

# 내 풀이


def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
            return False

    return True

# 다른 사람 풀이


def solution2(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123","456","789"]
phone_book = ["12", "123", "1235", "567", "88"]

print(solution(phone_book))
