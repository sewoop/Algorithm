class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 삽입
    def insert(self, string):
        curr = self.head

        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node를 새로 생성
            if char not in curr.child:
                curr.child[char] = Node(char)
            
            # 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr = curr.child[char]
        # 문자열이 끝난 지점의 노드의 data 값에 해당 문자열 입력
        curr.data = string
    
    # 문자열이 존재하는 지 search
    def search(self, string):
        # 가장 아래에 있는 노드에서부터 탐색 시작
        curr = self.head
        for char in string:
            if char in curr.child:
                curr = curr.child[char]
            else:
                return False
        
        # 탐색이 끝난 후 해당 노드의 data값이 존재한다면
        # 문자가 포함되어 있단는 뜻이다.
        if curr.data != None:
            return True

    def start_with(self, prefix):
        curr = self.head
        words = []

        for p in prefix:
            if p in curr.child:
                curr = curr.child[p]
            else:
                return None

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

trie = Trie()
words = ["119", "97674223", "1195524421"]

for word in words:
    trie.insert(word)

# print(trie.search("119"))
print(trie.start_with("119"))