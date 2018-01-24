# Disjoint Sets as Data Structure

Here you will find the implementation of disjoint set with the main three operations (i.e. `create_set`, `find_set` and `union`) also I have written some extra utility functions.

## Disjoint set forest implementation:

[disjointset.py](https://github.com/amit-upadhyay-IT/next-py/blob/master/disjoint_set/disjointset.py) is implementation which includes path compression and order by rank.

### usage:
['./test_disjoint.py'](./test_disjointset.py) is the example testcase.

## Disjoint set Linked List implementation:

[disjointset2.py](https://github.com/amit-upadhyay-IT/next-py/blob/master/disjoint_set/disjointset2.py) is linked list implementation of disjoint set which given O(n) time for union in amortized analysis.

### usage
['./test_disjointset2.py'](./test_disjointset2.py) is the example testcase.

## Disjoint set optimized linked list implementation:

[disjointset3.py](https://github.com/amit-upadhyay-IT/next-py/blob/master/disjoint_set/disjointset3.py) is the optimized implementation using linked list. Here the amortized time for union operation is `O(1)` (when we perform `n` `create_set` operations followed by `n-1` `union` operation.)

### usage
['./test_disjointset3.py'](./test_disjointset3.py) is example testcase.


## How to use?

### install

To install you can download the file:

**to use the forest implementation of disjoint set**:

```
wget https://raw.githubusercontent.com/amit-upadhyay-IT/next-py/master/disjoint_set/disjointset.py
```

**or to use the linked list implementation**

```
wget https://raw.githubusercontent.com/amit-upadhyay-IT/next-py/master/disjoint_set/disjointset2.py
```

**or to use the linked list implementation with optimized union**

```
wget https://raw.githubusercontent.com/amit-upadhyay-IT/next-py/master/disjoint_set/disjointset3.py
```

#### import

Import the file you wish to use.

Example:

```
import disjointset
```

#### Create instance:

Example: if you have download disjointset.py file, then:

```
disjoint = disjointset.DisjointSet(dict())
```

You need to pass a `dict()` object because the code is using a dictionary for doing data to node mapping in the disjoint set.

## Operations:

### Create set:

**Example**:

```
disjoint.create_set(20)
```

In the above example `20` is the data which is the member (representative) of the set.


### Union:

**Example**:

```
disjoint.union(10, 20)
```

unites the two set.

### Find Set:

**Example**:

```
disjoint.find_set(20)
```
`find_set` returns the representative element for the set containing `20`.
