import random
import time
import numpy as np
import matplotlib.pyplot as plt
import sys

def insertion_sort(arr: list) -> list:
    res = arr

    for i in range(1, len(arr)):
        key = res[i]

        j = i - 1
        while j >= 0 and key < res[j]:
            res[j+1] = res[j]
            j -= 1

        res[j+1] = key

    return res


times = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]
recorded_time = []
for i in range(len(times)):
    test = []
    for _ in range(times[i]):
        test.append(random.randint(1,20))

    start = time.process_time()
    res = insertion_sort(test)
    end = time.process_time() - start
    recorded_time.append(end)
    # print("It took", str(end) + "s", "to run selection_sort")

print(recorded_time)


x = np.asarray(times)
y = np.asarray(recorded_time)

plt.plot(x, y)
plt.savefig("new.png")
