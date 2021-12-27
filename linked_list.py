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

    def search(self, key):
        """
        This adds the ability to search for a particular point in
        linked list. This time complexity is O(n)
        """
        current = self.head
        while current:
            if current.data == key:
                # assuming we want the actual node object
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Inserts a new node containing data at
        index position. Insertion takes constant
        time but finding the node at insertion point
        takes linear time. Therefor overall linear time.
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            
            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1

            previous_node = current
            next_node = current.next_node

            previous_node.next_node = next_node

    def remove(self, key):
        """
        removes Node matching key
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position+=1

            return current

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
                components.append(f"[Head: {current.data}]")
            elif current.next_node:
                components.append(f"[{current.data}]")
            else:
                components.append(f"[Tail: {current.data}]")
            current = current.next_node
        return ' -> '.join(components)
        
