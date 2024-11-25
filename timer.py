import main
import time
import random

print('Bubble sort')
for t in range(2, 5):
    print('10^' + str(t))
    Massiv = [random.randint(1,100000) for i in range(10 ** t)]
    Start = time.time()
    main.bubble_sort(Massiv)
    Finish = time.time()
    time1 = (Finish - Start) * 1000
    print(time1)

print('Selection sort')
for k in range(2, 5):
    print('10^' + str(k))
    arr = [random.randint(1,100000) for i in range(10 ** k)]
    Start = time.time()
    main.selection_sort(arr)
    Finish = time.time()
    time2 = (Finish - Start) * 1000
    print(time2)

print('Insertion sort')
for p in range(2, 5):
    print('10^' + str(p))
    arrus = [random.randint(1,100000) for i in range(10 ** p)]
    Start = time.time()
    main.insertion_sort(arrus)
    Finish = time.time()
    time3 = (Finish - Start) * 1000
    print(time3)

print('Quick sort')
for s in range(2, 5):
    print('10^' + str(s))
    arrayich = [random.randint(1,100000) for i in range(10 ** s)]
    Start = time.time()
    main.quicksort(arrayich)
    Finish = time.time()
    time4 = (Finish - Start) * 1000
    print(time4)