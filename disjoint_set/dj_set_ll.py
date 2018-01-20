'''
disjoing set in linkedlist representation

Operations:
    1. create set
    2. find set
    3. union
'''


class Node:
    # important properties of Node is data, next_node and index_ptr
    def __init__(self, index_ptr=None, data=None, next_node=None):
        self.index_ptr = index_ptr
        self.data = data
        self.next_node = next_node


class IndexNode:
    # the identity of IndexNode is head and tail
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


class DisjointSet:
    # a dict is needed to store the address of representative of each set
    def __init__(self, node_map=None):
        self.node_map = node_map

    def create_set(self, data):
        # create the index node
        indexnode = IndexNode()
        # create a node for one member of a set
        node = Node(indexnode, data)  # sets the index_ptr, data and next_node

        # the head and tail of the Index Node should point to only node present
        indexnode.head = node
        indexnode.tail = node

        # store the address of representative into the dictionary
        self.node_map[data] = indexnode.head  # or node(since both are same)

    def find_set(self, data):
        if data in self.node_map:
            node = self.node_map[data]
            return node.index_ptr.head  # returns the representative of set
        else:  # returninig None as we don't found such data in set
            return None

    def union(self, data1, data2):

        # getting the nodes for corresponding data
        node1 = self.find_set(data1)  # node1 is representative of set1
        node2 = self.find_set(data2)  # node2 is representative of set2

        # I will append the set2 at end of set1
        # setting the set1 tail next pointer to head of set2
        node1.index_ptr.tail.next_node = node2.index_ptr.head
        # Also, I have to change the tail of set1 to tail of set2
        node1.index_ptr.tail = node2.index_ptr.tail

        # setting the index_ptr of each node in set2 to indexnode of set1
        temp = node2
        while temp.next_node is not None:
            temp.index_ptr = node1.index_ptr
            temp = temp.next_node
        # while doing union of sets with 1 member the next_node will be None
        # so, directly above while wouldn't execute
        else:
            temp.index_ptr = node1.index_ptr


if __name__ == '__main__':
    dj = DisjointSet(dict())
    dj.create_set('f')
    dj.create_set('g')
    dj.create_set('d')

    print dj.find_set('g').data  # g

    dj.create_set('c')
    dj.create_set('h')
    dj.create_set('e')
    dj.create_set('b')

    print dj.find_set('e').data  # e

    dj.union('f', 'g')
    dj.union('g', 'd')

    print dj.find_set('d').data  # f

    dj.union('f', 'c')
    dj.union('g', 'h')
    dj.union('f', 'e')
    dj.union('g', 'b')

    print dj.find_set('h').data  # f
    print dj.find_set('b').data  # f
