# Quick Sort algorithm to sort list in ascending order.
# Used unwanted variables just to make code more easy to understand.


def partition(unsorted_list, start_index, end_index):
    """
    Partition the list with smaller elements on left of pivot and greater elements on right of pivot
    Returns - pivot pointer - calculated index of pivot element
    """
    left_pointer = start_index - 1
    right_pointer = start_index
    # setting pivot as end index
    pivot = end_index
    # scan elements until pivot is reached
    while right_pointer < pivot:
        # if element at right_pointer is smaller than element at pivot,
        # increment left_pointer and swap the elements at right & left pointer
        if unsorted_list[right_pointer] < unsorted_list[pivot]:
            left_pointer = left_pointer + 1
            # swap elements
            temp = unsorted_list[left_pointer]
            unsorted_list[left_pointer] = unsorted_list[right_pointer]
            unsorted_list[right_pointer] = temp
        # increment right pointer
        right_pointer = right_pointer + 1

    # Now at this point - (right_pointer = pivot)
    # Now swap the elements at (pivot/right_pointer) with (left_pointer + 1)
    # set the pivot to (left_pointer + 1)
    # Now we will be having list like
    # ['elements smaller than pivot element', 'pivot element', 'elements greater than pivot element']
    temp = unsorted_list[pivot]
    unsorted_list[pivot] = unsorted_list[left_pointer + 1]
    unsorted_list[left_pointer + 1] = temp
    pivot = left_pointer + 1
    return pivot


def quick_sort(unsorted_list, start_index, end_index):
    """
    Quick Sort, sorts the list in ascending order
    """
    if start_index < end_index:
        pivot_index = partition(unsorted_list, start_index, end_index)
        quick_sort(unsorted_list, start_index, pivot_index - 1)
        quick_sort(unsorted_list, pivot_index + 1, end_index)


# Sample example
unsorted_list = [1, 5, 7, 0, 2, 4, -3, 8, 6, -2, 3, 9, -1]
size = len(unsorted_list)
quick_sort(unsorted_list, 0, size - 1)
print unsorted_list
