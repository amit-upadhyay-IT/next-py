# Graphs

## Graph: adjacency list implementation

### Types:

- Directed Graph

- UnDirected Graph

## Directed Graph

class : `DiGraph`

### instantiation:

```py
digraph = graphs.DiGraph(dict())
```

`dict()` is passed because this is adjacency list representation, so a dictionary will be used to map the node value with the list representing the adjacency list.


### Add edge:

```py
digraph.add_edge('a', 'b', 1)
```

'a' is source node, 'b' is destination node and `1` is weight of the edge between source node and destination node.


### print graph:

```py
digraph.print_graph()
```

Prints the graphs nodes in adjacency list representation.


### Bredth First Traversal:

```py
digraph.bft()
```

Traverse the graph in bredth wise manner.

### Depth First Traversal:

```py
digraph.dft()
```

Traverse the graph in depth manner.

## Un-directed Graph

class : `Graph`

### instantiation:

```py
graph = graphs.Graph(dict())
```

`dict()` is passed because this is adjacency list representation, so a dictionary will be used to map the node value with the list representing the adjacency list.


### Add edge:

```py
graph.add_edge('a', 'b', 1)
```

- 'a' is source node, 'b' is destination node and `1` is weight of the edge between source node and destination node.
- 'b' is source node, 'a' is destination node and `1` is weight of the edge between source node and destination node.


### print graph:

```py
graph.print_graph()
```

Prints the graphs nodes in adjacency list representation.


### Bredth First Traversal:

```py
graph.bft()
```

Traverse the graph in bredth wise manner.

### Depth First Traversal:

```py
graph.dft()
```

Traverse the graph in depth manner.
