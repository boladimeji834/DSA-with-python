print("This is a new linked list: ")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node_data, data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node and cur_node.data != prev_node_data:
            cur_node = cur_node.next
        if cur_node is None:
            print("The specified node is not in the list.")
            return
        new_node.next = cur_node.next
        cur_node.next = new_node

#     The delete method
    def delete_node(self, key):
        cur_node = self.head

        # Case: The node to be deleted is the head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        # Case: The node to be deleted is not found
        if cur_node is None:
            print("The key is not present in the list.")
            return

        # Unlink the node from the linked list
        prev.next = cur_node.next
        cur_node = None


if __name__ == "__main__":
    # Create a linked list
    llist = LinkedList()

    # Append nodes to the linked list
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")

    # Print the linked list
    print("Linked List:")
    llist.print_list()
    llist.delete_node("C")
    llist.print_list()