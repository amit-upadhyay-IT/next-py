class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    # identitiy of queue is front pointer and rare pointer
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    # inserts new node at the rear end of the queue
    def enqueue(self, data):
        # create a new node
        node = Node(data)
        if self.rear is not None:
            # add the node at the end of rear
            self.rear.next_node = node
            self.rear = node
        else:
            # i.e. no elements yet has been inserted into queue
            self.rear = self.front = node

    # removes and returns data of the node pointed by front in the queue
    def dequeuq(self):
        # check if some element is present in queue or not
        if self.front is None:
            return None
        # get the node pointer by front so that you can return it
        node = self.front
        self.front = self.front.next_node
        # if front now becomes None, then we need to set the rear as None too
        if self.front is None:
            self.rear = None
        return node.data

    # returns True is queue is empty else returns False
    def is_empty(self):
        if self.front is None and self.rear is None:
            return True
        else:
            return False

    # returns data of node being pointed by front ptr
    def get_front(self):
        return self.front.data

    # returns data of node being pointed by rear pointer
    def get_rear(self):
        return self.rear.data
