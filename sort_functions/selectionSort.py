# -------------------------------------------------------------------------
# Function: selectionSort(aList)
# Description: Takes a list as input, and sorts it via Selection Sort
# -------------------------------------------------------------------------
def selectionSort(aList):

    size = len(aList)

    # Traverse through the list
    for j in range(size):

        # Find the smallest element in the unsorted part of the list
        minIndex = j
        
        for k in range(j+1, size):
            if aList[minIndex] > aList[k]:
                minIndex = k

        # Move the smallest element to the first position
        temp = aList[j]
        aList[j] = aList[minIndex]
        aList[minIndex] = temp
