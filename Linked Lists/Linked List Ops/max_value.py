print("Finding the maximum value in a linked list: ")
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from traversing_singly_linked_list import *
def max_value(head):
    current_node = head
    max_value = current_node.data
    while current_node != None:
        if current_node.data > max_value:
            max_value = current_node.data
        current_node = current_node.next
    return max_value


print(max_value(node1))