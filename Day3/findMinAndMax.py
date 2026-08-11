def findMinAndMax(list):
    if not list:
        return None, None

    min = list[0]
    max = list[0]

    for i in list:
        if i < min:
            min = i
        if i > max:
            max = i

    return min, max


L = [2, 4, -1, 10, 13, 7]
print(findMinAndMax(L))
