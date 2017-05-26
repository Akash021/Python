def quicksort(alist,low,high):

    if low<high:
        split = partition(alist,low,high)

        quicksort(alist,low,split-1)
        quicksort(alist,split+1,high)

def partition(alist,low,high):

    pivot = alist[high]

    i = low-1
    for j in range(low,high):
        if alist[j] <= pivot:
            i = i+1
            alist[i],alist[j] = alist[j],alist[i]
    alist[i+1],alist[high] = alist[high],alist[i+1]
    return i+1

alist = [54,26,93,17,77,31,44,55,20]
n = len(alist)

quicksort(alist,0,n-1)

print (alist)