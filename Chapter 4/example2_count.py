def count(list):
    """
    递归列表计数
    """
    if list == []:
        return 0
    else:
        return 1 + count(list[1:])


print(count([1,2,3,4,5,6,7]))
