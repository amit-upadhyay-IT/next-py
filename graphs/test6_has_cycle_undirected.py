import graphs


if __name__ == '__main__':

    graph = graphs.Graph(dict())
    graph.add_edge('a', 'b', 1)
    graph.add_edge('b', 'c', 1)
    graph.add_edge('c', 'd', 1)
    graph.add_edge('d', 'a', 1)

    print graph.print_graph()

    if graph.has_cycle():
        print '\nThe above Graph has cycle'
    else:
        print '\nThe above Graph has no cycle'

    graph2 = graphs.Graph(dict())
    graph2.add_edge(1, 2, 1)
    graph2.add_edge(1, 3, 1)
    graph2.print_graph()
    if graph2.has_cycle():
        print '\nThe above graph has cycle'
    else:
        print '\nThe above graph has no cycle'
