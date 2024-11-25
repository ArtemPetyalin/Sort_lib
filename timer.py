import main
import time
import random
Massiv = [random.randint(1,100000) for i in range(100)]
Start = time.time()
main.insertion_sort(Massiv)
Finish = time.time()
Res_msec = (Finish - Start) * 1000
print(Res_msec)
