# Disjoint Sets as Data Structure

Here you will find the implementation of disjoint set with the main three operations (i.e. `create_set`, `find_set` and `union`) also I have written some extra utility functions.

## Disjoint set forest implementation:

[disjointset.py](https://github.com/amit-upadhyay-IT/next-py/blob/master/disjoint_set/disjointset.py) is implementation which includes path compression and order by rank.
['./test_disjoint.py'](./test_disjoint) is the example testcase.

## Disjoint set Linked List implementation:

[disjointset2.py](https://github.com/amit-upadhyay-IT/next-py/blob/master/disjoint_set/disjointset2.py) is linked list implementation of disjoint set which given O(n) time for union in amortized analysis.
['./test_disjointset2.py'](./test_disjointset2) is the example testcase.

## Disjoint set optimized linked list implementation:

[disjointset3.py](https://github.com/amit-upadhyay-IT/next-py/blob/master/disjoint_set/disjointset3.py) is the optimized implementation using linked list. Here the amortized time for union operation is `O(1)` (when we perform `n` `create_set` operations followed by `n-1` `union` operation.)
['./test_disjointset3.py'](./test_disjointset3.py) is example testcase.
