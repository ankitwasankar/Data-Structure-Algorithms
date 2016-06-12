# selection sort algorithm to sort in ascending order
def selection_sort(unsorted_list):
    size = len(unsorted_list)
    # Select the index from 0 to n-1 one by one
    for i in range(size - 1):
        # initialy the smallest_element values set to value at current index
        smallest_element = unsorted_list[i]
        smallest_element_index = i
        # flag to check if smallest element found other than current index
        flag = 0
        # compare all values from (index to n) & find index of smallest element
        for index in range(i, size):
            value_at_index = unsorted_list[index]
            if smallest_element > value_at_index:
                smallest_element = value_at_index
                smallest_element_index = index
                flag = 1
        # swap the element if flag=1 (if smallest element found)
        if flag == 1:
            temp = unsorted_list[i]
            unsorted_list[i] = unsorted_list[smallest_element_index]
            unsorted_list[smallest_element_index] = temp
    # After successful selection and swapping of all element return list
    return unsorted_list

# Sample example
unsorted_list = [1, 5, 7, 0, 2, 4, -3, 8, 6, -2, 3, 9, -1]
print selection_sort(unsorted_list)
