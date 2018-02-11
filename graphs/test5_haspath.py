import graphs

'''
    v2    v5
      \  /
       v1
      /  \
    v3<---v4
      \  /
       v6
Each edge has downward direction
'''


if __name__ == '__main__':

    digraph = graphs.DiGraph(dict())
    # agrs: src, dest, weight
    digraph.add_edge('v2', 'v1', 1)
    digraph.add_edge('v5', 'v1', 1)
    digraph.add_edge('v1', 'v3', 1)
    digraph.add_edge('v1', 'v4', 1)
    digraph.add_edge('v3', 'v6', 1)
    digraph.add_edge('v4', 'v6', 1)
    digraph.add_edge('v4', 'v3', 1)

    print 'For Graph:'
    digraph.print_graph()

    if digraph.has_path('v2', 'v3'):
        print '\nThere is path between v2 and v3'
    else:
        print '\nThere is no path between v2 and v3'

    print '\nFor Graph:'
    graph = graphs.Graph(dict())
    graph.add_edge('a', 'b', 1)
    graph.add_edge('b', 'c', 1)
    graph.add_edge('c', 'd', 1)
    graph.add_edge('d', 'a', 1)

    print graph.print_graph()

    if graph.has_path('a', 'c'):
        print '\nThere is path between a and c'
    else:
        print '\nThere is no path between a and c'
