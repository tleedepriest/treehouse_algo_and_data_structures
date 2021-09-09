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

class LinkedList:
    # instead of head = None here, we are going
    # to put in the construtor of the class.

    def __init__(self):
        """
        Initialize the Linked List empty, this is why head not in
        constructor
        """
        self.head = None

    def is_empty(self):
        """
        Simple assignment so O(1) time complexity. 
        If no Head, linked list empty
        """
        return self.head == None

    # here, while he was explaining it, I was a bit confused bc we hadn't
    # seen how the add method would work. Imagine that the Linked List has
    # data and it makes more sense
    def size(self):
        """
        count the number of nodes in the LinkedList
        O(n) time complexity
        """
        # current is Class Node
        current = self.head
        count = 0
        while current:
            current = current.next_node
            count+=1
        return count

    def add(self, data):
        """
        will add data to the front of the list, redefining the head
        and pushing the head of the list up one
        O(1) time complexity since just using assignment statements!
        """
        # this will be the new head
        new_node = Node(data)
        # make the next node the head
        new_node.next_node = self.head
        self.head = new_node

    def __repr__(self):
        pass

        
