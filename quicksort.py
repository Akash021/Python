def quicksort(alist):
    quicksorthelper(alist,0,len(alist)-1)

def quicksorthelper(alist,first,last):

    if first<last:
        split = partition(alist,first,last)

        quicksorthelper(alist,first,split-1)
        quicksorthelper(alist,split+1,last)

def partition(alist,first,last):

    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark+1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark+1

        if leftmark>rightmark:
            done = True

        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


alist = [54,26,93,17,77,31,44,55,20]

quicksort(alist)

print (alist)




