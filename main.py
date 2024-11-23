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

    def sorter(listofor):
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


            listofor = less_arr + [str(a) + 's'] + bigger_arr

        return listofor

    for i in range(len(l)):
        counter = 0
        index1 = 0
        print('run')
        for j in range(len(l)):

            if str(l[j])[-1] == 's' and j != index1:

                if j - index1 > 2:
                    l = l[:index1 + 1] + sorter(l[index1 + 1:j]) + l[j:]
                    counter += 1
                    index1 = j
                    print(l)

                if j - index1 == 2:
                    l[j - 1] = str(l[j - 1]) + 's'
                    index1 = j
                    counter += 1

                elif j - index1 == 1:
                     index1 = j
                     counter += 1

            elif j == len(l) - 1 and str(l[j]) != 's':
                l = l[:index1 + 1] + sorter(l[index1 + 1:])
                print(l)

    return l

print([5,4,1,2,8,9,0,414,13,11,54,52,61,87])
print(quick_sort([5,4,1,2,8,9,0,414,13,11,54,52,61,87]))







