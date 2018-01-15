import sll


if __name__ == '__main__':
    linkedlist = sll.LinkedList(sll.Node(5))  # creation of a node in SLL
    linkedlist.add_node(4)
    linkedlist.add_node(3)
    linkedlist.add_node(2)
    linkedlist.print_linkedlist()
