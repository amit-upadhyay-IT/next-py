'''
disjoing set in linkedlist representation

Operations:
    1. create set
    2. find set
    3. union

In this implementation the amortized time for union is O(n), but this time
can be improved to O(1) amortized time by keeping track of count of members
in the set. Coz, while performing union we can merge the smaller set at the
end of larger set (so time for changing the index_ptr will get reduced)
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
        self.sets_list = list()

    # creates a set containing one member, t.c = O(1)
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

        # adding the set to sets_list
        self.sets_list.append(indexnode.head)  # adding representative in list

    # finds the representative of member, t.c = O(1)
    def find_set(self, data):
        if data in self.node_map:
            node = self.node_map[data]
            return node.index_ptr.head  # returns the representative of set
        else:  # returninig None as we don't found such data in set
            return None

    # unites the two set, takes O(n) amortized time (cost per operation)
    def union(self, data1, data2):

        # getting the nodes for corresponding data
        node1 = self.find_set(data1)  # node1 is representative of set1
        node2 = self.find_set(data2)  # node2 is representative of set2

        # check if both data1 and data2 belong to same set or not
        if node1 == node2:
            return

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

        # remove the set2 from the sets_list
        self.sets_list.remove(node2)

    # returns all the sets present in DisjointSet
    def get_sets(self):
        return self.sets_list
