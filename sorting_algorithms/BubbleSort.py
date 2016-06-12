# Bubble Sort algorithm to sort in ascending order
# using unwanted variables just to make code more easy to understand


def bubble_sort(unsorted_list):
    size = len(unsorted_list)
    # sort one element in one iteration starting from last to start position
    # (size-1) is the last index of list and 0 is the start index
    # below syntax in c-language will be for(i=size-1; i>0; i--)
    for i in range((size - 1), 0, -1):
        # now compare each element with its previous element
        # in c-language below loop will be for(index=1; index <=i ; i++)
        for index in range(1, i + 1):
            # store previous element and current element
            current_element = unsorted_list[index]
            previous_element = unsorted_list[index - 1]
            # if previous element is greater than current then swap
            if previous_element > current_element:
                # swap the values
                temp = unsorted_list[index]
                unsorted_list[index] = unsorted_list[index - 1]
                unsorted_list[index - 1] = temp
    # After iterating through the list, we will get the sorted list
    # unsorted_list is sorted now
    return unsorted_list

# Sample example
unsorted_list = [1, 5, 7, 0, 2, 4, -3, 8, 6, -2, 3, 9, -1]
print bubble_sort(unsorted_list)
