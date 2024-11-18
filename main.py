def bubble_sort(listochek):

    for i in range(len(listochek)):

        for j in range(len(listochek) - i - 1):

            if listochek[j] > listochek[j + 1]:
                listochek[j], listochek[j + 1] = listochek[j + 1], listochek[j]

    return listochek


def selection_sort(listium):

    for i in range(len(listium)):

        for j in range(i, len(listium)):
            minimus = listium[j]

            if listium[j] < minimus:
                minimus = listium[j]

        listium[i] = minimus

    return listium


def insertion_sort(listus):

    for i in range(1, len(listus)):

        if listus[i - 1] < listus[i]:
            a = listus[i]
            j = i - 1

            while listus[j] > listus[i]:
                j -= 1

            listus.pop(i)
            listus.insert(j + 1, a)

    return listus

def quick_sort(l):

    if len(l) <= 1:
        return l

    indexer = []
    counter = 1
    def sorter(listofor):
        import random

        if len(listofor) > 1:
            a = random.choice(listofor)
            less_arr = []
            bigger_arr = []
            for i in range(len(listofor)):

                if listofor[i] >= a:
                    bigger_arr.append(listofor[i])

                else:
                    less_arr.append(listofor[i])

            less_arr.append(a)
            result = less_arr + bigger_arr
            less_arr.pop(-1)

            index_inside = len(listofor) - len(bigger_arr)

        return [a, index_inside]

    for i in range(len(l) // 2 + 1):






