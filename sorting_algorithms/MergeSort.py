# Merge Sort algorithm to sort in ascending order.
# Used unwanted variables just to make code more easy to understand.


def merge(unsorted_list, start_index, middle_index, end_index):
    """
    Merge two list
    """
    left_list = unsorted_list[start_index:middle_index + 1]
    right_list = unsorted_list[middle_index + 1: end_index + 1]
    pointer = start_index
    # start pointer for left list & right list
    left_start = 0
    right_start = 0
    # end pointer for left list and right list
    left_end = len(left_list) - 1
    right_end = len(right_list) - 1

    # merge left_list and right_list
    while left_start <= left_end and right_start <= right_end:
        if left_list[left_start] <= right_list[right_start]:
            unsorted_list[pointer] = left_list[left_start]
            left_start = left_start + 1
            pointer = pointer + 1
        else:
            unsorted_list[pointer] = right_list[right_start]
            right_start = right_start + 1
            pointer = pointer + 1

    # merge remaining left list, if any
    while left_start <= left_end:
        unsorted_list[pointer] = left_list[left_start]
        left_start = left_start + 1
        pointer = pointer + 1

    # merge remianing right list if any
    while right_start <= right_end:
        unsorted_list[pointer] = right_list[right_start]
        right_start = right_start + 1
        pointer = pointer + 1


def merge_sort(unsorted_list, start_index, end_index):
    """
    Sort the list in ascending order
    """
    if start_index < end_index:
        middle_index = (start_index + end_index) / 2
        merge_sort(unsorted_list, start_index, middle_index)
        merge_sort(unsorted_list, middle_index + 1, end_index)
        merge(unsorted_list, start_index, middle_index, end_index)


# Sample example
unsorted_list = [1, 5, 7, 0, 2, 4, -3, 8, 6, -2, 3, 9, -1]
size = len(unsorted_list)
merge_sort(unsorted_list, 0, size - 1)
print unsorted_list
