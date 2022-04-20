

def repetitionCount(lst):
    arr = []
    j = 1
    for i in lst:
        seq = filter(lambda x: x == i, lst)
        arr.append(len(seq))
    arr.sort()

    size = len(arr)
    while j != size:
        if arr[j] == arr[j - 1]:
            del arr[j]
            size -= 1
            j -= 1
        j += 1
    return arr


def distribution(lst, arr):
    n = 0
    result = []
    arr = arr[::-1]
    for j in arr:
        elemList = []
        for i in lst:
            seq = filter(lambda x: x == i, lst)
            if len(seq) == j:
                elemList.append(i)
        elements = [int(i) for i in elemList]
        result.append(elements)
        n += 1
    print(result)


if __name__ == '__main__':
    lst = [1, 2, 7, 1, 3, 2, 4, 7, 2, 1]
    arr = repetitionCount(lst)
    distribution(lst, arr)
