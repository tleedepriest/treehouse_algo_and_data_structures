from math import floor

# TODO: Replace slicing with binary search to reduce time complexity
def split(a_list):
    """
    divide a_list into sublists, left and right.
    at midpoint

    Returns left, right both Lists

    Takes O(k log(n)) time
    """
    midpoint = floor(len(a_list) / 2)
    left = a_list[:midpoint]
    right = a_list[midpoint:]
    return left, right

def merge(left_list, right_list):
    """
    merges and sorts in process

    Runs in overall linear time, takes n mumber
    of merge steps.
    """
    l = []
    i = 0
    j = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            l.append(left_list[i])
            i+=1
        else:
            l.append(right_list[j])
            j+=1
    
    # takes care of odd length lists
    while i < len(left_list):
        l.append(left_list[i])
        i+=1

    # left list is shorter than right
    while j < len(right_list):
        l.append(right_list[j])
        j+=1

    return l


def merge_sort(a_list):
    """
    sorts the list in ascending order
    Returns new sorted list
    Divide: find the midpoint of the list and divide into sublists
    Conquer: recursively sort the sublists
    Combine: merge sorted sublists

    O(k*n log(n)) time complexity
    O(n) space complexity
    """
    if len(a_list) <= 1:
        return a_list

    left_half, right_half = split(a_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def verify_sorted(a_list):
    """
    verifies whether the list is sorted
    """
    list_length = len(a_list)

    if list_length == 0 or list_length == 1:
        return True

    return a_list[0] <= a_list[1] and verify_sorted(a_list[1:])

if __name__ == "__main__":
    a_list = [34, 3, 24, 76, 8, 3, 54, 7, 8 ,234,35,567554, 34, 4]
    l = merge_sort(a_list)
    print(l)
    verify = verify_sorted(l)
    print(verify)
