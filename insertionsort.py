def insertionsort(lst):
    for i in range(1,len(lst)):
        key = lst[i]
        j = i-1

        while j > -1 and key < lst[j]:
            lst[j+1] = lst[j]
            j = j-1

        lst[j+1] = key



lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]

insertionsort(lst)

print "the sorted list using insertion sort is :"
for i in range(len(lst)):
    print "%d" %(lst[i]),


