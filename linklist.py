class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        #create a new node
        new_Node = Node(new_data)
        #create a link to the first node
        new_Node.next = self.head
        #make the new node the head of the LinkedList
        self.head = new_Node

    def insertAfter(self,prev_node,new_data):
        #create a node with the new data
        new_Node = Node(new_data)
        #make link from  new_Node to the next node
        new_Node.next = prev_node.next
        #make link from prev_node to new_Node
        prev_node.next = new_Node


    def append(self,new_data):
        #create a new node
        new_Node = Node(new_data)

        #Make new node as head if list is empty
        if self.head is None:
            self.head = new_Node
            return

        #else traverse till the last node
        last = self.head
        while(last.next):
            last = last.next

        #after reaching the last node,create a link from the last to the new new_Node
        last.next = new_Node



    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next



if __name__=='__main__':

    #start with an empty LinkedList

    llist = LinkedList()

    #Insert 6 .so LinkedList becomes 6->None
    llist.append(6)

    #Insert 7 at the beginning

    llist.push(7)

    #inser 1 at the beginning

    llist.push(1)

    #Insert 4 athe end

    llist.append(4)

    #Insert 8 after 7

    llist.insertAfter(llist.head.next,8)

    print "created linked list is:",
    llist.printList()
