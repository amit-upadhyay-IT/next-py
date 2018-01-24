class Node:
    # a node is required to have a data field and next_node address field
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    # the identity of a stack is the top (i.e. pointer pointing to top element)
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top  # sets the previous nodes after new_node
        self.top = new_node

    # returns the popped element if successfully done, otherwise returns False
    def pop(self):
        if self.is_empty():
            return False
        popped = self.top
        self.top = self.top.next_node
        return popped.data

    # returns True if the stack is empty else returns False
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    # returns element at top of stack, if not present then it returns False
    def peek(self):
        if self.is_empty():
            return False
        else:
            return self.top.data
