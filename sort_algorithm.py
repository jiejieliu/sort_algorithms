import operator
import numpy as np


def bubble_sort(array):
    flag = len(array)
    while flag:
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        flag = flag - 1
    return array


def selection_sort(list_aa):
    arry = [0] * len(list_aa)
    for i in range(len(list_aa)):
        min_number = min(list_aa)
        min_index = list_aa.index(min(list_aa))
        arry[i] = min_number
        del list_aa[min_index]
    return arry


def insert_sort(array_c):
    n = len(array_c)
    for i in range(1, n):
        if array_c[i] < array_c[i - 1]:
            temp = array_c[i]
            index = i
            for j in range(i - 1, - 1, -1):
                if array_c[j] > temp:
                    array_c[j + 1] = array_c[j]
                    index = j
                else:
                    break
            array_c[index] = temp
    return array_c


def shell_sort(array_d):
    n = len(array_d)
    step = round(n / 2)
    while step > 0:
        for i in range(step, n):
            temp = array_d[i]
            j = i
            while (j >= step and array_d[j - step] > temp):
                array_d[j] = array_d[j - step]
                j = j - step
            array_d[j] = temp
        step = round(step / 2)
    return array_d


def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = round(len(lists) / 2)
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


def quick_sort(array):
    return qsort(array, 0, len(array) - 1)


def qsort(array, left, right):
    if left >= right:
        return array
    key = array[left]
    lp = left
    rp = right
    while lp < rp:
        while array[rp] >= key and lp < rp:
            rp -= 1
        while array[lp] <= key and lp < rp:
            lp += 1
        array[lp], array[rp] = array[rp], array[lp]
    array[left], array[lp] = array[lp], array[left]
    qsort(array, left, lp - 1)
    qsort(array, rp + 1, right)
    return array


def head_sort(array):
    n = len(array)
    first = int(n / 2 - 1)
    for start in range(first, -1, -1):
        max_heapify(array, start, n - 1)
    for end in range(n - 1, 0, -1):
        array[end], array[0] = array[0], array[end]
        max_heapify(array, 0, end - 1)
    return array


def max_heapify(array, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and array[child] < array[child + 1]:
            child = child + 1
        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break


if __name__ == '__main__':
    array_a = np.array([4, 3, 2, 1])
    array_b = np.array([4, 3, 2, 1])
    array_c = np.array([4, 3, 2, 1])
    array_d = np.array([13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10])
    array_e = np.array([6, 5, 3, 1, 8, 7, 2, 4])
    print(array_a, array_b, array_c, array_d)

    bubble_arrray = bubble_sort(array_a)
    print(bubble_arrray)

    list_b = array_b.tolist()
    select_list = selection_sort(list_b)
    print(select_list)

    insert_array = insert_sort(array_c)
    print(insert_array)

    shell_array = shell_sort(array_d)
    print(shell_array)

    list_e = array_e.tolist()
    merge_array = merge_sort(list_e)
    print(merge_array)

    quick_array = quick_sort(array_d)
    print(quick_array)

    heap_array = head_sort(array_a)
    print(heap_array)
