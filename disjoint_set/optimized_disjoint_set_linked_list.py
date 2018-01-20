'''
disjoing set in linkedlist representation with count as property of IndexNode
using for counting the members in a set

Operations:
    1. create set
    2. find set
    3. union
    4. get sets

Here amortized time for union is O(1)
'''


class Node:
    # important properties of Node is data, next_node and index_ptr
    def __init__(self, index_ptr=None, data=None, next_node=None):
        self.index_ptr = index_ptr
        self.data = data
        self.next_node = next_node


class IndexNode:
    # the identity of IndexNode is head, tail and count
    def __init__(self, head=None, tail=None, count=None):
        self.head = head
        self.tail = tail
        self.count = count


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

        # setting the count of members in set
        indexnode.count = 1

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

    # unites the two set, takes O(1) amortized time (cost per operation)
    def union(self, data1, data2):

        # getting the nodes for corresponding data
        node1 = self.find_set(data1)  # node1 is representative of set1
        node2 = self.find_set(data2)  # node2 is representative of set2

        # check if both data1 and data2 belong to same set or not
        if node1 == node2:
            return

        # get count of members in set1 and set2
        count1 = node1.index_ptr.count
        count2 = node2.index_ptr.count

        # assuming that set1 is smaller
        smaller_set = node1
        larger_set = node2

        # if set 2 is smaller then setting appropriately
        if count1 > count2:
            smaller_set = node2
            larger_set = node1

        # I will append the smaller set at end of larger set
        # setting the larger_set tail next pointer to head of smaller_set
        larger_set.index_ptr.tail.next_node = smaller_set.index_ptr.head
        # Also, I have to change the tail of larger set to tail of smaller_set
        larger_set.index_ptr.tail = smaller_set.index_ptr.tail

        # setting the index_ptr of each node in set2 to indexnode of set1
        temp = smaller_set
        while temp.next_node is not None:
            temp.index_ptr = larger_set.index_ptr
            temp = temp.next_node
        # while doing union of sets with 1 member the next_node will be None
        # so, directly above while wouldn't execute
        else:
            temp.index_ptr = larger_set.index_ptr

        # remove the smaller_set from the sets_list
        self.sets_list.remove(smaller_set)

    # returns all the sets present in DisjointSet
    def get_sets(self):
        return self.sets_list
