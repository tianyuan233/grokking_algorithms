def max(list):
    if len(list) == 1:
        return list[0]
    return list[0] if list[0] > max(list[1:]) else max(list[1:])


print(max([1,2,9,23,6,4]))


