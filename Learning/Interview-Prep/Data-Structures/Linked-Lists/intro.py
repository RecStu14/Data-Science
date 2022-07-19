#INTRODUCTION TO LINKED LISTS

#Defining a Class - Node

from typing_extensions import Self

#Basic Building Unit of a Linked List
class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

class LinkedList(object):
    #takes in self and the root/head node, which defaults to None
    def __init__(self, r=None):
        self.root = r
        self.size = 0 #refers to the number of nodes in the LinkedLists

    def get_size(self):
        return self.size

    def add_node(self, d):
        #creating a new node with the data value and a root value of None initially
        new_node = Node(d, self.root) 
        #Allocating the self.root as the existing node
        self.root = new_node
        #Incrementing the size
        self.size += 1

    def remove_node(self, d):
        #keep track of 2 nodes as you need to change the pointer of the prev node
        this_node = self.root
        prev_node = None
        #iterate through the linked list
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                    self.size -= 1
                    return True #successfully removed data 

            else:
                prev_node = this_node
                this_node = this_node.get_next()
            return False #unsuccessfully removed -> need to add these indicators otherwise 
            #you wouldnt know if it is removed or not

    def find_node(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()

        return None
                
                

#Creating the Linked List
myLList = LinkedList()
myLList.add_node(5)
myLList.add_node(8)
myLList.add_node(12)
myLList.remove_node(8)
print(myLList.remove_node(12))
print(myLList.find_node(5))


    


