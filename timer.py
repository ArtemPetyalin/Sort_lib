import main
import time
import random

for t in range(2, 5):
    Massiv = [random.randint(1,100000) for i in range(10 ** t)]
    Start = time.time()
    main.insertion_sort(Massiv)
    Finish = time.time()
    time1 = (Finish - Start) * 1000
    print(time1)

for k in range(2, 5):
    arr = [random.randint(1,100000) for i in range(10 ** k)]
    Start = time.time()
    main.insertion_sort(arr)
    Finish = time.time()
    time2 = (Finish - Start) * 1000
    print(time2)

for p in range(2, 5):
    arrus = [random.randint(1,100000) for i in range(10 ** p)]
    Start = time.time()
    main.insertion_sort(arrus)
    Finish = time.time()
    time3 = (Finish - Start) * 1000
    print(time3)

for s in range(2, 5):
    arrayich = [random.randint(1,100000) for i in range(10 ** s)]
    Start = time.time()
    main.insertion_sort(arrayich)
    Finish = time.time()
    time4 = (Finish - Start) * 1000
    print(time4)