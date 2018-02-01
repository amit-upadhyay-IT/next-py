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
        # using a set to keep the count of vertices in graph
        self.vertices_set = set()

    # printing the adjacency list
    def print_graph(self):
        for key in self.node_dic:
            # get the list
            lis = self.node_dic[key]
            print key, '->', [str(i.vertex)+':'+str(i.weight) for i in lis]

    def vertices_count(self):
        return len(self.vertices_set)

    # bredth first traversal, time: O(v+e)
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
    # time complexity = O(v + e) or O(v + 2e)
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
            else:
                # since queue is not empty, so pop from queue & update v
                v = queue.pop(0)

    # depth first traversal: time = O(e+v) or O(2e+v)
    def dft(self):
        # initialize the visited dictionary. why is visited a dict?
        # coz, if I use list then to access members I can only use the index
        # in the list and the index is always a integer, so if the graph node
        # contains someother type of data, then using just list wouldn't work
        visited = dict()
        # iterate through all the vertices in the graph and add them in visited
        # since, it's not necessary that all vertices are present in node_dic,
        # (in case of some DAG)so, I will initiallize visited with vertices_set
        for v in self.vertices_set:
            # initilizing with False because initially none is visited
            visited[v] = False
        # iterate through the all the vertices and call the bfs
        for v in self.node_dic:
            if visited[v] is False:
                self.dfs(v, visited)
        print

    # depth first search, v is the vertex from where search starts
    # time complexity = O(v + e) or O(v + 2e)
    def dfs(self, v, visited):
        # set v in visited to True
        visited[v] = True
        # print the vertex
        print v,
        # get the adjacent nodes(i.e. adjacent list) for vertex v
        # from list I fetch vertex only
        # Also, in some cases adjacent_list may be None (eg, in DAG, all
        # vertices might not be in node_dic), so for loop will throw TypeError
        # in that case
        if v in self.node_dic:
            adjacent_list = [i.vertex for i in self.node_dic.get(v)]
            for w in adjacent_list:
                if w in visited and visited[w] is False:
                    # exploring the node without visiting other adjacent
                    self.dfs(w, visited)


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
        # why do I need to use extra memory for set to keep the count of
        # vertices in graph?
        # as in directed graph, we can have nodes with some indegree but zero
        # out-degree, so for that case we don't create an entry in node_dic
        # thus we miss out that vertex in the count, so I use a set here
        self.vertices_set.add(src)
        self.vertices_set.add(dest)

    # prints the elements in topological sorted manner
    # time = O(V*E),
    # Since, this implementation of adjacency list is done using lists of dict
    # so, the time complexity comes to O(EV), if I would have implemented the
    # graph using dictionary of dictionary, then this same approach will result
    # in O(V*V) time, as searching over the list time will get reducted
    # Even in the implementation of adjacency list we can improve time by using
    # queue
    def topological_sort2(self):
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

    # prints the elements in topological sorted manner
    # modified dft method
    # the idea behind this algo is given here: https://youtu.be/n_yl2a6n7nM
    # time: O(V+E), as this is just modified version of dft
    def topological_sort(self):
        # init a stack
        stack = list()
        # make visited dict
        visited = dict()
        # init visited with vertices_set
        for v in self.vertices_set:
            visited[v] = False
        # iterate throught the vertices
        for v in self.node_dic:
            if visited[v] is False:
                self.modified_dfs_for_top_sort(v, visited, stack)

        # pop from stack and print (i.e. print from end)
        for ind in xrange(len(stack)-1, -1, -1):
            print stack[ind],

    def modified_dfs_for_top_sort(self, v, visited, stack):
        visited[v] = True
        if v in self.node_dic:
            a_list = [i.vertex for i in self.node_dic.get(v)]
            for w in a_list:
                if w in visited and visited[w] is False:
                    self.modified_dfs_for_top_sort(w, visited, stack)
        # adding the vertex to stack here, because at this point of time the
        # vertex v has no more vertices to visit in dfs fashion, so
        stack.append(v)


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
        # vertices_set isn't necessarly required for un-directed graph, as its
        # purpose can be completed by node_dic, but still I have made it for
        # compatiblity with its parent class, coz someone may like using
        # vertices_set, insted of node_dic
        # NOTE: don't remove this coz my dft implementation uses this set to
        # initialize the visited dict
        self.vertices_set.add(src)
        self.vertices_set.add(dest)

    # since, this is un-directed graph, so src and dest both will have entry
    # in the node_dic, this is overridden function
    def vertices_count(self):
        return len(self.node_dic)
