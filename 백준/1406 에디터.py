# import sys

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class Deque:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.cursor = None

#     def __str__(self):
#         curr = self.head
#         lst = []
#         while curr:
#             lst.append(curr.data)
#             curr = curr.next

#         return ''.join(lst)

#     def insert(self, data):
#         newNode = Node(data)

#         if self.head == None:
#             self.head = newNode
#             self.tail = newNode
#             self.cursor = newNode
#             return

#         # cursor 중심
#         if self.cursor == None:
#             self.head.prev = newNode
#             newNode.next = self.head

#             self.head = newNode
#             self.cursor = newNode
#             return

#         elif self.cursor == self.tail:
#             newNode.prev = self.cursor
#             self.cursor.next = newNode
#             self.tail = newNode
#             self.cursor = newNode
#             return

#         else:
#             newNode.next = self.cursor.next
#             self.cursor.next.prev = newNode
#             newNode.prev = self.cursor
#             self.cursor.next = newNode

#             self.cursor = newNode
#             return

#     def delete(self):
#         # cursor 중심으로
#         # dx
#         if self.cursor == None:
#             return

#         elif self.head == self.tail:
#             self.tail = None
#             self.head = None
#             self.cursor = None
#             return

#         elif self.cursor == self.tail:
#             self.tail = self.cursor.prev
#             self.cursor.prev.next = None
#             self.cursor.prev = None
#             self.cursor = self.tail
#             return

#         elif self.head == self.cursor:
#             self.cursor.next.prev = None
#             self.head = self.cursor.next
#             self.cursor.next = None
#             self.cursor = None
#             return

#         else:
#             temp = self.cursor.prev
#             self.cursor.prev.next = self.cursor.next
#             self.cursor.next.prev = self.cursor.prev
#             self.cursor.next = None
#             self.cursor.prev = None
#             self.cursor = temp
#             return

#     def leftShift(self):
#         if self.cursor == None:
#             return
#         else:
#             self.cursor = self.cursor.prev

#     def rightShift(self):
#         if self.cursor != self.tail:
#             self.cursor = self.cursor.next

# deque = Deque()
# for i in list(sys.stdin.readline().replace('\n', '')):
#     deque.insert(i)
# n = int(sys.stdin.readline())

# # cursor = len(deque) # 4
# for _ in range(n):
#     control = sys.stdin.readline()
#     if 'P' in control:
#         _, dollar = control.split()
#         deque.insert(dollar)

#     elif 'L' in control:
#         deque.leftShift()

#     elif 'D' in control:
#         deque.rightShift()

#     elif 'B' in control:
#         deque.delete()

# print(deque)

from sys import stdin

stk1 = list(stdin.readline().strip())
stk2 = []
n = int(input())
for line in stdin:
    if line[0] == 'L':
        if stk1:
            stk2.append(stk1.pop())
        else:
            continue
    elif line[0] == 'D':
        if stk2:
            stk1.append(stk2.pop())
        else:
            continue
    elif line[0] == 'B':
        if stk1:
            stk1.pop()
        else:
            continue
    elif line[0] == 'P':
        stk1.append(line[2])

print(''.join(stk1 + list(reversed(stk2))))
