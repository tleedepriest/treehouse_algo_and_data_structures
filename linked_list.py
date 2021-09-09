"""
This script will implement a linked list from memory
"""

class Node:
    """
    Modeling a Node contained in Simply Linked List
    attributes of the node are the data within the node and the next_node
    it is linked to.
    """
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

    # just realized that this is what links the Node Class to the Linked List!
    # by using the class here, we guarantee that all values in the linked list
    # are Node objects..very cool.
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
        """
        This will be O(n) run time since it will have to itterate through
        all components
        """
        components = []
        current = self.head
        next_node = current.next_node
        while current:
            if current == self.head:
                components.append(f"Head: {current.data}")
            elif current.next_node:
                components.append(f"{current.data}")
            else:
                components.append(f"Tail: {current.data}")
            current = current.next_node
        return '-> '.join(components)
        
