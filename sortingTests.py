from sort_functions.bubbleSort import *
from sort_functions.insertionSort import *
from sort_functions.mergeSort import *
from sort_functions.quickSort import *
from sort_functions.selectionSort import *

import random
import time

# -------------------------------------------------------------------------
# Function: generateList(numElements)
# Description: Generates and returns an array of size numElements
# -------------------------------------------------------------------------
def generateList(numElements):
    newList = []
    
    for i in range(numElements):
        newList.append(random.randint(1,100001))

    return newList


# -------------------------------------------------------------------------
# Function: bubbleSortTest()
# Description: Creates random lists of varying sizes (2.5k - 20k elements)
#              and prints the amount of time it takes to sort the elements
#              using Bubble Sort
# -------------------------------------------------------------------------
def bubbleSortTest():

    testCases = [2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000]
    print("Now performing Bubble Sort tests...")
    print("======================RESULTS======================")

    for item in testCases:
        aList = generateList(item)
        startTime = time.time()
        bubbleSort(aList)
        elapsedTime = round((time.time() - startTime), 4)
        print("Time to sort", item , "elements is", elapsedTime, "seconds")

    print("===================================================")

# -------------------------------------------------------------------------
# Function: insertionSortTest()
# Description: Creates random lists of varying sizes (2.5k - 20k elements)
#              and prints the amount of time it takes to sort the elements
#              using Insertion Sort
# -------------------------------------------------------------------------
def insertionSortTest():

    testCases = [2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000]
    print("Now performing Insertion Sort tests...")
    print("======================RESULTS======================")

    for item in testCases:
        aList = generateList(item)
        startTime = time.time()
        insertionSort(aList)
        elapsedTime = round((time.time() - startTime), 4)
        print("Time to sort", item , "elements is", elapsedTime, "seconds")

    print("===================================================")

# -------------------------------------------------------------------------
# Function: selectionSortTest()
# Description: Creates random lists of varying sizes (2.5k - 20k elements)
#              and prints the amount of time it takes to sort the elements
#              using Selection Sort
# -------------------------------------------------------------------------
def selectionSortTest():

    testCases = [2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000]
    print("Now performing Selection Sort tests...")
    print("======================RESULTS======================")

    for item in testCases:
        aList = generateList(item)
        startTime = time.time()
        selectionSort(aList)
        elapsedTime = round((time.time() - startTime), 4)
        print("Time to sort", item , "elements is", elapsedTime, "seconds")

    print("===================================================")

# -------------------------------------------------------------------------
# Function: mergeSortTest()
# Description: Creates random lists of varying sizes (2.5k - 20k elements)
#              and prints the amount of time it takes to sort the elements
#              using Merge Sort
# -------------------------------------------------------------------------
def mergeSortTest():

    testCases = [50000, 100000, 150000, 200000, 250000, 300000,
                 350000, 400000]
    print("Now performing Merge Sort tests...")
    print("======================RESULTS======================")

    for item in testCases:
        aList = generateList(item)
        startTime = time.time()
        mergeSort(aList)
        elapsedTime = round((time.time() - startTime), 4)
        print("Time to sort", item , "elements is", elapsedTime, "seconds")

    print("===================================================")

# -------------------------------------------------------------------------
# Function: quickSortTest()
# Description: Creates random lists of varying sizes (2.5k - 20k elements)
#              and prints the amount of time it takes to sort the elements
#              using Quick Sort
# -------------------------------------------------------------------------
def quickSortTest():

    testCases = [50000, 100000, 150000, 200000, 250000, 300000,
                 350000, 400000]
    print("Now performing Quick Sort tests...")
    print("======================RESULTS======================")

    for item in testCases:
        aList = generateList(item)
        startTime = time.time()
        quickSort(aList)
        elapsedTime = round((time.time() - startTime), 4)
        print("Time to sort", item , "elements is", elapsedTime, "seconds")

    print("===================================================")
