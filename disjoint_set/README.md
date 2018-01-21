# Disjoint Sets as Data Structure

Here you will find the implementation of disjoint set with the main three operations (i.e. `create_set`, `find_set` and `union`) also I have written some extra utility functions.

## Disjoint set forest implementation:

[disjointset.py]() is implementation which includes path compression and order by rank.

## Disjoint set Linked List implementation:

[disjointset2.py]() is linked list implementation of disjoint set which given O(n) time for union in amortized analysis.

## Disjoint set optimized linked list implementation:

[disjointset3.py]() is the optimized implementation using linked list. Here the amortized time for union operation is `O(1)` (when we perform `n` `create_set` operations followed by `n-1` `union` operation.)


# TODO:

- Optimize the design, or ask a question for its perfect design on stackexchange review.

