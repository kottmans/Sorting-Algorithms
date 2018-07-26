# -------------------------------------------------------------------------
# Function: bubbleSort(aList)
# Description: Takes a list as input, and sorts it via Bubble Sort
# -------------------------------------------------------------------------
def bubbleSort(aList):
    n = len(aList)

    # Go through each element in the list
    for j in range(n):

        # Stop at n-j-1, as proceeding elements are already sorted
        swapped = False
        for k in range(0, n-j-1):

            # swap elements if the next element is greater
            # if we swap, set our flag "swapped" to True
            if aList[k] > aList[k+1]:
                temp = aList[k]
                aList[k] = aList[k+1]
                aList[k+1] = temp
                swapped = True

        # if we don't swap, it means the list is sorted
        if swapped == False:
            break
