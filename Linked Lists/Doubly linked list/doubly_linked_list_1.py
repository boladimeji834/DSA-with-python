print("Implementation of Doubly Linked List")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(4)
node2 = Node(6)
node3 = Node(10)
node4 = Node(90)

node1.next = node2
node2.next = node3
node3.next = node4


node4.prev = node3
node3.prev = node2
node2.prev = node1

currentNode = node1

# Traversing forward in the linked list
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

# traversing backward in the linked list

currentNode = node4
while currentNode:
    print(currentNode.data, end="-> ")
    currentNode = currentNode.prev

print("null")