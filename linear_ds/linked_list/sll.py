class Node:

    # the identity of a node is data and next_node address
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:

    # head is refering to the top node in the LinkedList, head is the identity
    def __init__(self, head=None):
        self.head = head

    # add_node is same as insertion at beginning
    def add_node(self, data):
        new_node = Node(data)
        new_node.next_node = self.head  # setting the head to newly formed node
        self.head = new_node

    def print_linkedlist(self):
        temp = self.head
        while temp is not None:
            print temp.data,
            temp = temp.next_node
        print
