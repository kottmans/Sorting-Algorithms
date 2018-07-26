# -------------------------------------------------------------------------
# Function: insertionSort(aList)
# Description: Takes a list as input, and sorts it via Insertion Sort
# -------------------------------------------------------------------------
def insertionSort(aList):

    size = len(aList)

    # Traverse through the list
    for j in range(1, size):
        
        firstUnsorted = aList[j]

        # move first unsorted element into sorted section
        k = j-1

        while k >= 0 and firstUnsorted < aList[k]:
            aList[k+1] = aList[k]
            k -= 1

        aList[k+1] = firstUnsorted
