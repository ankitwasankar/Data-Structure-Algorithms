# Radix Sort algorithm to sort list in ascending order.
# Used unwanted variables just to make code more easy to understand.
# works only for whole numbers


def counting_sort(unsorted_list, divisor):
    # decalring lists
    list_0 = []
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    list_6 = []
    list_7 = []
    list_8 = []
    list_9 = []

    # count sort according to divisor
    for element in unsorted_list:
        digit = ((element % divisor) / (divisor / 10))
        if digit == 0:
            list_0.append(element)
        elif digit == 1:
            list_1.append(element)
        elif digit == 2:
            list_2.append(element)
        elif digit == 3:
            list_3.append(element)
        elif digit == 4:
            list_4.append(element)
        elif digit == 5:
            list_5.append(element)
        elif digit == 6:
            list_6.append(element)
        elif digit == 7:
            list_7.append(element)
        elif digit == 8:
            list_8.append(element)
        elif digit == 9:
            list_9.append(element)

    # holding temporary values
    temp = (list_0 + list_1 + list_2 + list_3 + list_4 +
            list_5 + list_6 + list_7 + list_8 + list_9)
    return temp


def radix_sort(unsorted_list):
    """
    Radix sort will sort the list in ascending order
    """
    # say 123 is the greatest number
    greatest_number = max(unsorted_list)
    # digits in number are 3
    digits_in_number = len(str(abs(greatest_number)))
    divisor = 10
    # sort by digits recursively
    while digits_in_number > 0:
        unsorted_list = counting_sort(unsorted_list, divisor)
        divisor = divisor * 10
        digits_in_number = digits_in_number - 1

    return unsorted_list


# Sample example
unsorted_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print radix_sort(unsorted_list)
