# Exercise 2, q1-3

import sys
import json
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

# open and load the contents of the file
with open("ex2q2.json", "r") as file:
    contents = json.load(file)

    arr_of_times = []
    input_labels = ["input 1", "input 2", "input 3", "input 4", "input 5", "input 6", "input 7", "input 8", "input 9", "input 10", ]
    for input in contents:
        size = len(input)
        start = time.time()
        func1(input, 0, size - 1)
        end = time.time()
        arr_of_times.append(end - start)
    print(arr_of_times)


    plt.plot(input_labels, arr_of_times)
    plt.title("Inputs vs Time Taken")
    plt.xlabel("Inputs")
    plt.ylabel("Time Taken (s)")
    plt.show()
