def binary_search(alist,key):
    low = 0
    high = len(alist)-1

    while low <= high:
        mid = (low + high)/2

        if alist[mid] == key:
            return mid
        elif key > alist[mid]:
            low = mid + 1
        elif key < alist[mid]:
            high = mid - 1
    return -1

testlist = [21,33,44,56,66,36,76,86,96,106,111]

print (binary_search(testlist,76))


