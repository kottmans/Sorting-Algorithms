# -------------------------------------------------------------------------
# Function: mergeSort(aList)
# Description: Takes a list as input, and sorts it via Merge Sort
# -------------------------------------------------------------------------
def mergeSort(aList):
    size = len(aList)

    if size > 1:
        # split original list into left and right halves
        middle = size // 2
        left = aList[:middle]
        right = aList[middle:]

        # recursively call mergeSort
        mergeSort(left)
        mergeSort(right)

        # Merge the lists back together
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                aList[k] = left[i]
                i += 1
            else:
                aList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            aList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            aList[k] = right[j]
            j += 1
            k += 1
