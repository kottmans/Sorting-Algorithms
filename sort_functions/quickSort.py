# -------------------------------------------------------------------------
# Function: quickSort(aList)
# Description: Takes a list as input, and sorts it via Quick Sort
# -------------------------------------------------------------------------
def quickSort(aList):
   quickSortHelper(aList, 0, len(aList)-1)

def quickSortHelper(aList, first, last):
   if first < last:

       split = partition(aList, first, last)

       quickSortHelper(aList, first, split - 1)
       quickSortHelper(aList, split + 1,last)


def partition(aList,first,last):
   pivot = aList[first]

   left = first+1
   right = last

   done = False
   while not done:

       while left <= right and aList[left] <= pivot:
           left = left + 1

       while aList[right] >= pivot and right >= left:
           right = right -1

       if right < left:
           done = True
       else:
           temp = aList[left]
           aList[left] = aList[right]
           aList[right] = temp

   temp = aList[first]
   aList[first] = aList[right]
   aList[right] = temp


   return right
