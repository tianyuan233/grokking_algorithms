def binary_search(list, item):
    """
    二分查找
    :param list:
    :param item:
    :return:
    """
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


list = [1, 3, 5, 7, 9, 12]

print(binary_search(list, 12))
