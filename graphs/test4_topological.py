import graphs_lib_test

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

    digraph = graphs_lib_test.DiGraph(dict())
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
