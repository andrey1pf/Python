import json
import time
import csv

from sortings import bubbleSort, insertionSort, shellSort, selectionSort, mergeSort, quickSort, quickSortHoare


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def timeSort():
    with open("Input.json") as inp:
        tampung = json.load(inp)
    n = len(tampung)

    with open("Statistics.csv", "w") as out:
        csv_out = csv.writer(out)
        csv_out.writerow(["Algorithm", "Time"])
        for i in range(0,n):
            item = tampung[i]
            arr = item['Marks']
            average = 0
            for j in range(0, len(arr)):
                average += arr[j]
            average = average / len(arr)
            array = []
            array.append(average)
        start = time.time()
        bubbleSort(array)
        end = time.time()
        csv_out.writerow(["Bubble Sort", end-start])
        start = time.time()
        insertionSort(array)
        end = time.time()
        csv_out.writerow(["Insertion Sort", end-start])
        start = time.time()
        shellSort(array)
        end = time.time()
        csv_out.writerow(["Shell Sort", end-start])
        start = time.time()
        selectionSort(array)
        end = time.time()
        csv_out.writerow(["Selection Sort", end-start])
        start = time.time()
        mergeSort(array)
        end = time.time()
        csv_out.writerow(["Merge Sort", end-start])
        start = time.time()
        quickSort(array)
        end = time.time()
        csv_out.writerow(["Quick Sort", end-start])
        start = time.time()
        quickSortHoare(array)
        end = time.time()
        csv_out.writerow(["Quick Sort Hoare", end-start])


def sortJSON():
    with open("Input.json") as inp:
        tampung = json.load(inp)
    n = len(tampung)

    dictionary = {}
    sorted_dictionary = {}
    array = []
    for i in range(0,n):
        item = tampung[i]
        arr = item['Marks']
        average = 0
        for j in range(0, len(arr)):
            average += arr[j]
        average = average / len(arr)
        dictionary[item['ID']] = average
        array.append(average)
    sorted_array = shellSort(array)
    for i in range(0,n):
        sorted_dictionary[get_key(dictionary, sorted_array[i])] = sorted_array[i]
    with open("Output.json", "w") as out:
        out.write("[")
        for j in range(0,n):
            for i in range(0,n):
                item = tampung[i]
                id = item['ID']
                if id == get_key(dictionary, sorted_array[j]):
                    json.dump(item, out)
                    if i != n-1:
                        out.write(",\n")
                    else:
                        out.write("]")
                    break


if __name__ == '__main__':
    print("[+] Sorting JSON...")
    sortJSON()
    print("[+] Check Input.json")
    print("[+] Sorting Time...")
    timeSort()
    print("[+] Check Statistics.csv")
    print("[+] Done")