
from timeit import Timer
import random
from matplotlib import pyplot as plt

def analyze(fxn, data):
    times = []
    for d in data:
        t = Timer(lambda : fxn(d[:]))
        time = t.timeit(number = 1)
        times.append(time)
    return times

# define the sorting algorithms to be tested
def bubbleSort(items):
    for i in range(len(items)-1, 0, -1):                        # generate a range for the next step
        for j in range(i):                                      # note that the range i is decrementing
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j] # swap items

def mergeSort(items):
    if len(items) > 1:
        mid = len(items) // 2
        l = items[:mid]
        r = items[mid:]
        mergeSort(l)
        mergeSort(r)
        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):
            if l[ i] <= r[ j]:
                items[ k] = l[ i]
                i += 1
            else:
                items[ k] = r[ j]
                j += 1
            k += 1
        while i < len(l):
            items[ k] = l[ i]
            i, k = i + 1, k + 1
        while j < len(r):
            items[ k] = r[ j]
            j, k = j + 1, k + 1

if __name__ == "__main__":
    # generate lists of random numbers from 0 to 500
    d1 = random.sample(range(0, 500), 10)
    d2 = random.sample(range(0, 500), 20)
    d3 = random.sample(range(0, 500), 50)
    d4 = random.sample(range(0, 500), 100)
    d5 = random.sample(range(0, 500), 200)

    # use random lists as input
    data = [d1, d2, d3, d4, d5]

    # measure the time taken by bubbleSort on each input
    bubbleSort_times = analyze(bubbleSort, data)

    # measure the time taken by mergeSort on each input
    mergeSort_times = analyze(mergeSort, data)

    # plot the results
    plt.plot([len(i) for i in data], bubbleSort_times, "r", label = "bubbleSort")
    plt.plot([len(i) for i in data], mergeSort_times, "b", label = "mergeSort")
    plt.legend()
    plt.xlabel("Input size")
    plt.ylabel("Time (seconds)")
    plt.show()
