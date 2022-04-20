# coding=utf-8
import array as arr


def sortByName(lst):
    lst.sort(key=lambda x: x.lower())
    return lst


def sortByExtension(lst):
    lst.sort(key=lambda x: x.split('.')[-1])
    return lst


def dopSort(lst):
    for q in range(0, len(lst)):
        for i in range(len(lst)):
            if i != len(lst) - 1:
                x = lst[i]
                y = lst[i + 1]
                if x.split('.')[-1] == y.split('.')[-1]:
                    if x.lower() > y.lower():
                        lst[i] = y
                        lst[i + 1] = x
    return lst


if __name__ == '__main__':
    lst = ["taest.py", "tf.est2.py", "td.e.s.t3.py", "tces.t.txt", "ta.e.s.t3.py", "test.cs", "tb.est.cpp"]
    lst = sortByExtension(lst)
    print("sort by extension with name: ", dopSort(lst))


