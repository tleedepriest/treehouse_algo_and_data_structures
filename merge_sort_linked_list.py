"""................
apply data structure and algoirthms so far
"""
from linked_list import LinkedList

def split(linked_list):
    """
    divide linked_list at subpoint and return sublists
    """
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    
    else:
        size = linked_list.size() 
        print(size)
        mid = size // 2

        # size always returns value 1 greater than max index value
        mid_node = linked_list.node_at_index(mid-1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        
        return left_half, right_half

def merge(left, right):
    """
    Merges two linked list, sorting by data in the nodes
    Returns a new merged list
    """
    # create new linked list that contains nodes merging
    # left and right
    merged = LinkedList()
    # add fake head that is discarded later
    merged.add(0)

    # set current to head of the linked list
    current = merged.head
    print(f"top of loop{current}")
    # obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # itterate over left and right until we reach the tail node
    # of eigther
    while left_head or right_head:
        
        # if head node of left is None, we're past the tail
        # add teh node from rigth to merged linked list
        print(f"right_head{right_head}") 
        print(f"left head{left_head}")
        
        if left_head is None:
            current.next_node = right_head
            # call next on right to set left head loop condition to False
            right_head = right_head.next_node
        
        # if head node of right is None, we're past the tail
        # add the tail node from left to merged linked list
        
        elif right_head is None:
            current.next_node = left_head
            # call next on left to set right head loop condition to False
            left_head = left_head.next_node

        else:
            # not at either tail node 
            # obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to
            # left node
            if left_data < right_data:
                current.next_node = left_head
                # move left head to next node
                left_head = left_head.next_node
            # if data on left is greater than right,
            # set current to right node


            # If data on left > thatn right, set current to
            # right node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        current = current.next_node
        print(f"current: {current}")
    #Discard fake head and set first merged node as head

    head = merged.head.next_node
    merged.head = head
    return merged

def merge_sort(linked_list):
    """
    Sorts a LinkedList in ascending order
     - 
     Recursively divide linked list into sublists
        containing single Node
    -
    Repeatedly merge sublists into sorted sublists
        until one remains
    -
    Returns sorted linked list
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    print(f"LINKED LIST HEAD {linked_list.head}")
    left_half, right_half = split(linked_list)
    
    print(left_half)
    print(right_half)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

l = LinkedList()
l.add(20)
l.add(39)
l.add(3)
l.add(564)

print(l)
print(merge_sort(l))
