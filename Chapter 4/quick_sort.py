def quickSort(arr):
    """
    快速排序
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        small = [i for i in arr[1:] if i <= pivot]
        big = [i for i in arr[1:] if i > pivot]
        return quickSort(small) + [pivot] + quickSort(big)

print(quickSort([34,5,9,2]))
