'''
disjoint set forest implementation
'''


class Node:
    # the identity of node(member of set) is given by data, parent_link, rank
    def __init__(self, data=None, rank=None, parent_link=None):
        self.data = data
        self.rank = rank
        self.parent_link = parent_link


class DisjointSet:
    # dictionary is important here because here I need to map data to node
    def __init__(self, node_map):
        self.node_map = node_map

    # create a new set i.e create a node, make it point to itself and set rank
    def create_set(self, data):
        node = Node(data, 0)  # setting the data and rank
        node.parent_link = node  # since its the only node in the set
        self.node_map[data] = node  # creating the data to node mapping

    # returns the data contained in the representative_node
    def find_set(self, data):
        # getting the node containing data
        node = self.node_map[data]
        representative_node = self.find_representative(node)
        return representative_node.data

    # returns the representative_node of the node passed as agrument in fun
    # this method is also responsible for path compression, here I am using
    # recusive approach to perform the path compression
    def find_representative(self, node):
        # getting the parent of the given node
        parent = node.parent_link
        # check if the parent is the root (i.e. representative_node) or not
        if parent == node:  # if root, then parent will be same as node
            return parent
        # set the parent_link of each node in the path to the root
        node.parent_link = self.find_representative(node.parent_link)
        return node.parent_link

    # performs the union using using by rank method
    def union(self, data1, data2):
        # get the node corrosponding to data1 and data2
        node1 = self.node_map[data1]
        node2 = self.node_map[data2]

        # check if both data1 and data2 belongs to same set or not
        # for this I need to know the representative_node of each data1 & data2
        rep1 = self.find_representative(node1)
        rep2 = self.find_representative(node2)
        if rep1.data == rep2.data:
            return False  # False indicates, there is not need to perform union

        # the tree with higher rank should become the final representative_node
        if rep1.rank >= rep2.rank:
            # if rank of both set is same then final rank will increase by 1
            # else the rank would be same as rep1's rank
            rep1.rank = 1 + rep1.rank if rep1.rank == rep2.rank else rep1.rank

            # set the parent_link of set2 to representative_node of set1
            rep2.parent_link = rep1
        else:
            # setting the parent_link of set1 to representative_node of set2
            rep1.parent_link = rep2
        return True  # represents that union happened successfully
