"""
This script will implement a linked list from memory
"""

class Node:
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"
