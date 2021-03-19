# List

class List:
    def __init__(self):
        self.list = []
        self.pos = 0
        self.size = 0

    def append(self, data):
        self.list.append(data)
        self.size += 1

    def find(self, data):
        for i in range(self.size):
            if self.list[i] == data:
                return i
        return False

    def insert(self, data, after):
        insert_position = self.find(after)
        if insert_position:
            self.list.insert(insert_position + 1, data)
            self.size += 1
            return True
        return False

    def remove(self, data):
        found_at = self.find(data)
        if found_at:
            del self.list[found_at]
            self.size -= 1
            return True
        return False

    def clear(self):
        self.list.clear()
        self.size = 0
        self.pos = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return f"[{', '.join(list(map(str, self.list)))}]"