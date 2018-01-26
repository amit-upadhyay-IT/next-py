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
