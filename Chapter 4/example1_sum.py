def sum(list):
    """
    递归列表求和    
    """
    if list == []:
        return 0
    else:
        return list[0] + sum(list[1:])


print(sum([1, 2, 3, 4, 5]))
