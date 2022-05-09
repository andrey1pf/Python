def checkExeption(arr, k):
    try:
        for i in range(len(arr)):
            a = int(arr[i])
    except ValueError:
        print("[-] Error, array contains different types")
        exit()
    if len(arr) == 0:
        print("[-] Error, array is empty")
        exit()
    if len(arr) == 1:
        return arr[0]
    if len(arr) < k:
        print("[-] Error, k is greater than the length of the array")
        exit()


def sepList(arr, left, right, q):
    p = arr[q]
    arr[q], arr[right] = arr[right], arr[q]
    i = left
    for j in range(left, right):
        if arr[j] <= p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def k_min(arr, k):
    left = 0
    right = len(arr) - 1
    if left == right:
        return arr[left]
    q = sepList(arr, left, right, (left + right) // 2)
    if q == k:
        return arr[q]
    if k < q:
        return k_min(arr[:q], k)
    elif k > q:
        return k_min(arr[q + 1:], k - q - 1)


if __name__ == '__main__':
    search_sequence = [10, True, 0, 2, 9]
    print("Enter k:")
    try:
        k = int(input())
    except ValueError:
        print("[-] Error, k1 is not an integer or empty")
        exit()

    print(f"[+] Search sequence: {search_sequence}")
    print(f"[+] k: {k}")
    checkExeption(search_sequence, k)
    print("[+] Searching...")
    print(f"[+] Result: {k_min(search_sequence, k - 1)}")