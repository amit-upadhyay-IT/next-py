'''
Graph implementation using adjacency list.
This file contains implementation of some algos on graph
'''


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
            print key, '->', [i.vertex for i in lis]

    # bredth first traversal
    def bft(self):
        # initialize the visited dictionary. why is visited a dict?
        # coz, if I use list then to access members I can only use the index
        # in the list and the index is always a integer, so if the graph node
        # contains someother type of data, then using just list wouldn't work
        visited = dict()
        # iterate through all the vertices in the graph and add them in visited
        for v in self.node_dic:
            # initilizing with False because initially none is visited
            visited[v] = False
        # iterate through the all the vertices and call the bfs
        for v in self.node_dic:
            if visited[v] is False:
                self.bfs(v, visited)
        print

    # bredth first search, v is the vertex from where the search starts
    def bfs(self, v, visited):
        # creating the queue
        queue = list()
        visited[v] = True
        # print first vertex
        print v,
        # repeating until the queue gets empty
        while True:
            # get the adjacent list for node 'v', from list I fetch vertex only
            adjacent_list = [i.vertex for i in self.node_dic.get(v)]
            for w in adjacent_list:
                # get the vertex from the adjacent node
                if visited[w] is False:
                    # add w to queue
                    queue.append(w)
                    # print w
                    print w,
                    # update the visited dict
                    visited[w] = True
            # if queue is empty then break the loop
            if len(queue) <= 0:
                break
            # since queue is not empty, so pop from queue & update v
            else:
                v = queue.pop(0)


# directed graph
class DiGraph(Gr):

    def __init__(self, node_dic=None):
        # calling the parent class constructor
        Gr.__init__(self, node_dic)

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


# un-directed graph
class Graph(Gr):

    def __init__(self, node_dic):
        # calling the parent class constructor
        Gr.__init__(self, node_dic)

    # method to create edge between the src and dest node with specified weight
    def add_edge(self, src, dest, weight):
        # since this is un-directed so I need to add for src as well as dest
        # first creating the edge from src to dest
        if src in self.node_dic:
            lis = self.node_dic.get(src)
            lis.append(Node(dest, weight))
        else:
            self.node_dic[src] = [Node(dest, weight)]
        # now creating edge from dest to src
        if dest in self.node_dic:
            lis = self.node_dic.get(dest)
            lis.append(Node(src, weight))
        else:
            self.node_dic[dest] = [Node(src, weight)]
