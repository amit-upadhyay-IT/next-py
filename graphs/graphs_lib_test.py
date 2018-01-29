# It is the representation of each vertex in the graph
class Node:
    # a node in graph is likely to have vertex, weight. Also, node_address ptr
    # is not required as I am gonna use in-built list
    def __init__(self, vertex=None, weight=None, next_node=None):
        self.vertex = vertex
        self.weight = weight


# a parent class for the different types of Graphs, this class is created
# to reuse the code snippets like print_graph, bfs and dfs, etc
class Gr(object):
    # In adjacency list representative I would need a mapper to map the node
    # value with the list representing the adjacency list (i.e. adjacent nodes)
    # so I use a dictionary to create data to list mapping
    def __init__(self, node_dic=None):
        self.node_dic = node_dic

    # printing the adjacency list
    def print_graph(self):
        for key in self.node_dic:
            # get the list
            lis = self.node_dic[key]
            print key, '->', [str(i.vertex)+':'+str(i.weight) for i in lis]


# directed graph
class DiGraph(Gr):

    def __init__(self, node_dic=None):
        # calling the parent class constructor
        Gr.__init__(self, node_dic)
        # using a set to keep the count of vertices in graph
        self.vertices_set = set()

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
        # why do I need to use extra memory for set to keep the count of
        # vertices in graph?
        # as in directed graph, we can have nodes with some indegree but zero
        # out-degree, so for that case we don't create an entry in node_dic
        # thus we miss out that vertex in the count, so I use a set here
        self.vertices_set.add(src)
        self.vertices_set.add(dest)

    def vertices_count(self):
        return len(self.vertices_set)

    # prints the elements in topological sorted manner
    # time = O(V*E + V), we can optimize this time by adding some other ds
    def topological_sort(self):
        print '\ntopological sort:'
        # run a loop untill graph is not empty
        while True:
            # get the node with indegree as zero
            for k in list(self.vertices_set):
                # check if conde containing k has indegree zero or not
                ret = self.check_vertex(k)
                if ret is not None:
                    # it's the node with indegree as zero
                    print k,
                    # now delete the entry containing k from dictionary
                    # note only delete if k is present in dic, otherwise you
                    # will face KeyError, checking will be constant time work
                    if k in self.node_dic:
                        del self.node_dic[k]
                    # also remove from the set
                    self.vertices_set.remove(k)
            if len(self.vertices_set) <= 0:
                    break

    # check if node containing 'v' has indegree zero or not
    # if indegree of node containing 'v' is zero then it must not be the
    # adjacent of any other vertex (i.e. it should not be present in any of the
    # list being pointed by the array of pointers i.e. dict value)
    # time = O(E), as we need to search for all elements in list pointed by dict
    # value
    def check_vertex(self, v):
        # keeping flag to indicate if we found node containing v or not
        flag = False
        # iterate though the lists in dictionary
        for key in self.node_dic:
            # get the list corrospoinding to the key
            lis = self.node_dic.get(key)
            if v in [i.vertex for i in lis]:
                # change flag and represent that v is found as adjacent
                flag = True
                # as we already found v somewhere as adjacent to no need to go
                # further, thus breaking out of the loop
                break
        if flag is False:
            return v  # itnicates node containing v has indegree as zero
        else:
            return None


'''
    v2    v5
      \  /
       v1
      /  \
    v3    v4
      \  /
       v6
'''


if __name__ == '__main__':

    digraph = DiGraph(dict())
    # agrs: src, dest, weight
    digraph.add_edge('v2', 'v1', 1)
    digraph.add_edge('v5', 'v1', 1)
    digraph.add_edge('v1', 'v3', 1)
    digraph.add_edge('v1', 'v4', 1)
    digraph.add_edge('v3', 'v6', 1)
    digraph.add_edge('v4', 'v6', 1)
    digraph.add_edge('v4', 'v3', 1)

    digraph.print_graph()
    digraph.topological_sort()
