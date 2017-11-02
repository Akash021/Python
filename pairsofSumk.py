def findPairs(list1,k):
    #initialise empty list to store the pair of numbers
    list2 = []
    sum1 = k
    list1.sort()
    #initialise the left and right indices of the list for traversal
    l = 0
    r = len(list1)-1

    #here we loop the list to find the pairs which add up sum1
    while l<r:
        if list1[l]+list1[r]>sum1:
            r -= 1
        elif list1[l]+list1[r]<sum1:
            l += 1
        elif list1[l]+list1[r]==sum1:

            list2.append((list1[l],list1[r]))
            l += 1
    #return the length of the list which contains the pairs of numbers
    list2 = list(set(list2))
    print list2
    return len(list2)


#driver program for the function
list1 = [6,6,3,4,9,2,1,5,8]
list3 = [1,2,3,3,4,4,5,6,7,8,9,9,0,10]
k1 = 12
k2 = 10
print findPairs(list1,k1)
print findPairs(list3,k2)
