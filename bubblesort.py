def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


arr = [64, 34, 25, 12, 22, 11, 90]

bubblesort(arr)

print "the sorted array is :"
for i in range(len(arr)):
    print "%d" %(arr[i]),


