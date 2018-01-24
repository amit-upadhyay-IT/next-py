import graphs

if __name__ == '__main__':
    digraph = graphs.DiGraph(dict())
    digraph.add_edge('a', 'b', 1)
    digraph.add_edge('a', 'd', 1)
    digraph.add_edge('b', 'a', 3)
    digraph.add_edge('b', 'c', 1)
    digraph.add_edge('c', 'b', 1)
    digraph.add_edge('c', 'd', 5)
    digraph.add_edge('d', 'c', 1)
    digraph.add_edge('d', 'a', 6)

    print 'printing the digraph'
    digraph.print_graph()
    print
    print 'bft:'
    digraph.bft()
    print 'dft:'
    digraph.dft()

    print '\nprinting the graph'
    graph = graphs.Graph(dict())
    graph.add_edge('a', 'b', 1)
    graph.add_edge('b', 'c', 1)
    graph.add_edge('c', 'd', 1)
    graph.add_edge('d', 'a', 1)

    graph.print_graph()

    print
    print 'bft:'
    graph.bft()
    print 'dft:'
    graph.dft()
