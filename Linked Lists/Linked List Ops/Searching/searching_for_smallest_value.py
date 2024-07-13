print("Searching for smallest value in linked list")
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from traversing_singly_linked_list import *

def find_smallest_value(head):
    current_node = head
    smallest_value = current_node.data

    while current_node != None:
        if current_node.data < smallest_value:
            smallest_value = current_node.data
        current_node = current_node.next
    return smallest_value




print(find_smallest_value(node1))


