"""
Attempt to write the code from video here without looking.
Heavy use of comments to document my thinking.
"""

# Define the problem.
# Binary search_must have sorted_list as input.
# complexity is Log(n) because of the halfing of tries on each iteration.

# output is the index of the target value in the list
def iter_binary_search(sorted_list, target):
    """
    Parameters
    -------------
    sorted_list: List[int]
        a list that is sorting in increasing order.

    target: int
        a number that is located in the list
    """
    first = 0 # define the start position of list
    last = len(sorted_list) - 1 # end position of list, offset one

    while first <= last: # think about this condition only after if,elif,else
        midpoint = (first + last) // 2
        
        # return the index of the value equal to the target in the list
        if sorted_list[midpoint] == target:
            return midpoint
        
        # if value at position midpoint less than target
        # ------midpoint_index--------target--------
        # increment first by one in order to move the
        # midpoint closer to the target.
        elif sorted_list[midpoint] < target:
            first = midpoint + 1

        # if value at position midpoint greater than target
        # ------target--------------midpoint_index---
        # subtract one from last in order to move
        # the midpoint closer to target
        else sorted_list[midpoint] > target:
            last = midpoint - 1
    
    # if the while loop completes, and surpasses the worst case
    # scenario of the binary_search algorithm, then the
    # the target is not a value in the list
    return None


if __name__ == "__main__":
    # TO-DO: write some simple tests to make sure algorithm works


