print("Searching for smallest value in linked list")
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from traversing_singly_linked_list import *

def find_smallest_value(head):
    smallest = head
    while smallest is not None:
        if head.next.data < smallest.data:
            smallest = smallest.next
    return smallest.data


print(find_smallest_value(node1))


