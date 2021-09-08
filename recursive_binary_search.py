"""
This will impelement the recursive version of the binary
search algorithm, which takes up O(log n) space complexity.

The iterative version is simply O(1) space complexity.
"""

# see iter_binary_search.py for problem desc.
# this will be a variation where we only return
# whether or not the target is located in the list
def rec_binary_search(sorted_list, target):
    """
    Parameters
    ------------
    sorted_list: List[int]
        a sorted list of integerts.

    target: int
        the value we are looking for in the list
    """
    # this is our base case, this means
    # if the list dwindles down to zero without
    # answer, no target found
    if len(sorted_list) == 0:
        return False
    else:
        # define variables as before
        first = 0
        last = len(sorted_list) - 1
        midpoint = first + last // 2
        if sorted_list[midpoint] == target:
            return True

        # ---- midpoint_index ---------- target
        # need to move midpoint up to get closer
        # to target...or rather...
        # slice beginning of list off
        elif sorted_list[midpoint] < target:
            return rec_binary_search(sorted_list[midpoint+1:], target)
        
        # ---------- target--------- midpoint_index-----
        # don't subtract one here, bc the last value in the list is
        # not included in python's syntax
        # again, need to move midpoint_index closer to target, 
        # or rather slice off the end of the list
        else:
            return rec_binary_search(sorted_list[:midpoint], target)

if __name__ == "__main__":
    #TO-DO: Write some tests here to test solution
