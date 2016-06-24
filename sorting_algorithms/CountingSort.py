# Counting Sort algorithm to sort in ascending order
# using unwanted variables just to make code more easy to understand


def counting_sort(unsorted_list):
    """
    Sort the list in ascending order
    """
    size = len(unsorted_list)
    # create the count array
    max_integer = max(unsorted_list)
    count_list = [0] * (max_integer + 1)
    # fill the counts in count_list
    for integer in unsorted_list:
        count_list[integer] = count_list[integer] + 1

    # generate counts as cummulative sum
    size = len(count_list)
    for i in range(1, size):
        count_list[i] = count_list[i - 1] + count_list[i]

    # sort the unsorted_list into output_list
    output_list = [0] * len(unsorted_list)
    for i in reversed(unsorted_list):
        output_list[count_list[i] - 1] = i
        count_list[i] = count_list[i] - 1

    return output_list

# Sample example
unsorted_list = [1, 5, 7, 0, 2, 4, 8, 6, 3, 99]
print counting_sort(unsorted_list)
