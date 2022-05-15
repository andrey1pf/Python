import math
from random import random


def bubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A


def insertionSort(A):
    for i in range(1, len(A)):
        j = i - 1
        element = A[i]
        while j >= 0 and A[j] < element:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = element
    return A


def shellSort(A):
    n = len(A)
    k = int(math.log2(n))
    gap = 2 ** k - 1
    while gap > 0:
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp
        k -= 1
        gap = 2 ** k - 1
    return A


def selectionSort(A):
    for i in range(len(A)):
        min = i
        for j in range(i+1, len(A)):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]
    return A


def quickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = [elem for elem in A if elem < q]
        M = [q] * A.count(q)
        R = [elem for elem in A if elem > q]
        return quickSort(L) + M + quickSort(R)


def quickSortHoare(A):
    if len(A) <= 1:
        return A
    else:
        low = 0; high = len(A) - 1
        mid = (low + high) // 2
        if A[low] > A[mid]:
            A[low], A[mid] = A[mid], A[low]
        if A[mid] > A[high]:
            A[mid], A[high] = A[high], A[mid]
        if A[low] > A[mid]:
            A[low], A[mid] = A[mid], A[low]
        q = A[mid]
        L = [elem for elem in A if elem < q]
        M = [q] * A.count(q)
        R = [elem for elem in A if elem > q]
        return quickSort(L) + M + quickSort(R)


def merge(A, B):
    Res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            Res.append(A[i])
            i += 1
        else:
            Res.append(B[j])
            j += 1
    Res += A[i:] + B[j:]
    return Res


def mergeSort(A):
    if len(A) <= 1:
        return A
    else:
        L = A[:len(A) // 2]
        R = A[len(A) // 2:]
    return merge(mergeSort(L), mergeSort(R))
