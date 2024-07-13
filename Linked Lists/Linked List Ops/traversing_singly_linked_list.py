print("Traversing Linked Lists")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Instantiating nodes from the Node class
node1 = Node(4)
node2 = Node(7)
node3 = Node(9)
node4 = Node(3)

# Links the nodes together
node1.next = node2
node2.next = node3
node3.next = node4

# Doing the traversal
# currentNode = node1
#
# while currentNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next
# print("None")