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
        a = listus[i]
        j = i - 1

        while j >= 0 and listus[j] > a:
            listus[j + 1] = listus[j]
            j -= 1

        listus[j + 1] = a

    return listus

def quicksort(listofor):
    import random

    if len(listofor) > 1:
        ind_a = random.randint(0, len(listofor) - 1)
        a = listofor[ind_a]
        listofor.pop(ind_a)
        less_arr = []
        bigger_arr = []
        for i in range(len(listofor)):

            if listofor[i] >= a:
                bigger_arr.append(listofor[i])

            else:
                less_arr.append(listofor[i])

        return quicksort(less_arr) + [a] + quicksort(bigger_arr)

    else:
        return listofor