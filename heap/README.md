# Heap

Module name: `heap.py`


## Classes:

### a) MinHeap:

- To instantiate:

```py
minheap = heap.MinHeap(heap_size, heap_list)
```

> heap_size is the number of nodes in the heap
> heap_list is the list using which the heap needs to be constructed

Just after creating the instance of MinHeap, you need to build the minheap by calling the
`build_heap()` function for the construction of the heap.

Example:

```py
# you have an optional argument here using which you can construct the
# heap according to some attribute of the object which is going to be stored
# in the heap
minheap.build_heap([attribute_name])  # attribute_name is optional
```

- To Heapify about some node:

Example:

```py
# the heapificaton takes place about the index passed in the argument
# the attribute_name argument is optional

minheap.min_heapify(index [, attribute_name])
```

- Get the minimum:

Example:

```py
# returns the node containing the minimum key
minheap.get_min()
```

- Remove minimum / Extract minimum

```py
# remove the node containing minimum key and returns that node
minheap.extract_min()
```


- Increase Key
