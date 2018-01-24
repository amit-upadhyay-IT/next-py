'''
         1
        /  \
       2    3
      / \  / \
     4  5,6   7
      \ | | /
         8
'''


import graphs

if __name__ == '__main__':

    digraph = graphs.DiGraph(dict())
    digraph.add_edge(1, 2, 1)
    digraph.add_edge(2, 1, 1)
    digraph.add_edge(1, 3, 1)
    digraph.add_edge(3, 1, 1)
    digraph.add_edge(2, 4, 1)
    digraph.add_edge(4, 2, 1)
    digraph.add_edge(2, 5, 1)
    digraph.add_edge(5, 2, 1)
    digraph.add_edge(3, 6, 1)
    digraph.add_edge(6, 3, 1)
    digraph.add_edge(3, 7, 1)
    digraph.add_edge(7, 3, 1)
    digraph.add_edge(4, 8, 1)
    digraph.add_edge(8, 4, 1)
    digraph.add_edge(5, 8, 1)
    digraph.add_edge(8, 5, 1)
    digraph.add_edge(6, 8, 1)
    digraph.add_edge(8, 6, 1)
    digraph.add_edge(7, 8, 1)
    digraph.add_edge(8, 7, 1)

    print 'printing the digraph'
    digraph.print_graph()
    print
    print 'bft:'
    digraph.bft()
    print 'dft:'
    digraph.dft()

    print '\nprinting the graph'
    graph = graphs.Graph(dict())
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 4, 1)
    graph.add_edge(2, 5, 1)
    graph.add_edge(3, 6, 1)
    graph.add_edge(3, 7, 1)
    graph.add_edge(4, 8, 1)
    graph.add_edge(5, 8, 1)
    graph.add_edge(6, 8, 1)
    graph.add_edge(7, 8, 1)

    graph.print_graph()

    print
    print 'bft:'
    graph.bft()
    print
    print 'dft:'
    graph.dft()
