# Exercise 2, q4

import sys
import json
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def modified_func1(arr, low, high):
    # for arrays less than 16 elements, use the insertion_sort function
    if high - low + 1 <= 25:
        return insertion_sort(arr, low, high)
    else:
        # for arrays with more than 16 elements, use regular quicksort
        pi = func2(arr, low, high)
        modified_func1(arr, low, pi-1)
        modified_func1(arr, pi+1, high)
        return arr
        
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high -= 1
        while low <= high and array[low] <= p:
            low += 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def insertion_sort(arr, low, high):
    for i in range(low+1, high+1):
        key = arr[i]
        j = i-1
        while j >= low and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

# open and load the contents of the file
with open("ex2q2.json", "r") as file:
    contents = json.load(file)

    arr_of_times = []
    input_labels = ["input 1", "input 2", "input 3", "input 4", "input 5", "input 6", "input 7", "input 8", "input 9", "input 10", ]
    for input in contents:
        size = len(input)
        start = time.time()
        modified_func1(input, 0, size - 1)
        end = time.time()
        arr_of_times.append(end - start)
    print(arr_of_times)

    plt.plot(input_labels, arr_of_times)
    plt.title("Inputs vs Time Taken")
    plt.xlabel("Inputs")
    plt.ylabel("Time Taken (s)")
    plt.show()