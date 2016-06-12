# Insertion Sort algorithm to sort in ascending order
# using unwanted variables just to make code more easy to understand


def insertion_sort(unsorted_list):
    # get the size of list
    size = len(unsorted_list)
    # first element is always sorted
    # starting loop from second element of list to last element
    for i in range(1, size):
        # check until element smaller than - element at index i, is found
        if unsorted_list[i] > unsorted_list[i - 1]:
            continue
        else:
            # if current element is smaller than previous
            # 1. find the location to insert current element
            index = i
            # Linear searching of index to insert
            # binary search can be used, but swapping can not be avoided
            # hence going with linear search
            while unsorted_list[index] < unsorted_list[index - 1] and index > 0:
                # swap the elements until appropriate position is found
                temp = unsorted_list[index]
                unsorted_list[index] = unsorted_list[index - 1]
                unsorted_list[index - 1] = temp
                index = index - 1
    # After iterating through the list, we will get the sorted list
    # unsorted_list is sorted now
    return unsorted_list


# Sample example
unsorted_list = [1, 5, 7, 0, 2, 4, -3, 8, 6, -2, 3, 9, -1]
print insertion_sort(unsorted_list)
