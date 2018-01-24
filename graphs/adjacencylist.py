'''
adjacency list implementation
'''


# It is the representation of each vertex in the graph
class Node:
    # a node in graph is likely to have vertex, weight. Also, node_address ptr
    # is not required as I am gonna use in-built list
    def __init__(self, vertex=None, weight=None, next_node=None):
        self.vertex = vertex
        self.weight = weight


# directed graph
class DiGraph:
    # In adjacency list representative I would need a mapper to map the node
    # value with the list representing the adjacency list (i.e. adjacent nodes)
    # so I use a dictionary to create data to list mapping
    def __init__(self, node_dic=None):
        self.node_dic = node_dic

    # this method adds the edge b/w src node to dest node with specified weight
    def add_edge(self, src, dest, weight):
        # check if src is present in node_dic or not
        if src in self.node_dic:
            # since it's present so get the list from map
            lis = self.node_dic.get(src)
            # now add the destination in the list for node src
            lis.append(Node(dest, weight))
        else:
            # as the src wasn't present in dictionary, so add it
            self.node_dic[src] = [Node(dest, weight)]

    # printing the adjacency list
    def print_graph(self):
        for key in self.node_dic:
            # get the list
            lis = self.node_dic[key]
            print key, '->', [i.vertex for i in lis]


if __name__ == '__main__':
    graph = DiGraph(dict())
    graph.add_edge('a', 'b', 1)
    graph.add_edge('a', 'd', 1)
    graph.add_edge('b', 'a', 3)
    graph.add_edge('b', 'c', 1)
    graph.add_edge('c', 'b', 1)
    graph.add_edge('c', 'd', 5)
    graph.add_edge('d', 'c', 1)
    graph.add_edge('d', 'a', 6)

    graph.print_graph()
