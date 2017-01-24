import time
from BubbleSortLab1 import bubblesort
from SelectionSortLab1 import selectionsort
from InsertionSortLab1 import insertionSort

# time for bubble sort
start_time = time.clock()

print(bubblesort([10000, -50, 0.0001, 100, 41, -9, 150]))
bubbletime = time.clock() - start_time
print("time taken for bubble sort", time.clock() - start_time, "seconds")

# time for selection sort
start_time = time.clock()

print(selectionsort([10000, -50, 0.0001, 100, 41, -9, 150]))

print("time taken for selection sort", time.clock() - start_time, "seconds")

# time for insertion sort
start_time = time.clock()

print(insertionSort([10000, -50, 0.0001, 100, 41, -9, 150]))

print("time taken for  insertion sort", time.clock() - start_time, "seconds")
