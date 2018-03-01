'''
implementation of head as a abstract ds
'''


# utility function which can be called once instead of checking the attr_name
# for None most of the places in the code below
def perform(obj, attr_name):
    if attr_name is None:
        return obj
    else:
        return getattr(obj, attr_name)


# parent class for MinHeap and MaxHeap, here the common utility functions
# are implemented
class Heap(object):
    # property of heap: a) heap_size and b) heap_list
    def __init__(self, heap_size=None, heap_list=None):
        self.heap_size = heap_size
        self.heap_list = heap_list

    # print the heap indexed from 1 to n, if you want to print a particular
    # attribute of the object stored in heap then while calling print_heap
    # you can pass the attribute name as the argument, it will print the
    # specifit property of the object in heap
    def print_heap(self, attr_name=None):
        for i in xrange(1, self.heap_size + 1):
            print perform(self.heap_list[i], attr_name),
        print

    def get_heap_size(self):
        return self.heap_size


class MinHeap(Heap):
    # constuctor for MinHeap, it should call the parent constructor
    def __init__(self, heap_size=None, heap_list=None):
        Heap.__init__(self, heap_size, heap_list)

    # heapify the MinHeap on the index passed as the arg
    # the indexing here is starts from 1, time complexity = O(log2(n))
    def min_heapify(self, i, attr_name=None):
        # step1: get the smallest among the left child, right child and root
        # step2: if root is not the smallest among three then swap appropriately

        # get left index
        left = i * 2
        # get right index
        right = i * 2 + 1

        # init the smallest var
        smallest = -1

        # check if left is greater than root, also check the boundary of left
        if left <= self.heap_size and perform(self.heap_list[left], attr_name)\
                < perform(self.heap_list[i], attr_name):
            smallest = left
        else:
            smallest = i

        # check if right is smallerst or not, also check the boundary of right
        if right <= self.heap_size and perform(self.heap_list[right], attr_name) < \
                perform(self.heap_list[smallest], attr_name):
            smallest = right

        # step 2: if smallest is not the one at root, then you need to swap
        if smallest != i:
            self.heap_list[smallest], self.heap_list[i] = \
                self.heap_list[i], self.heap_list[smallest]
            # after this swap there may be disordering somewhere in child
            # so again calling heapify over the smallest index
            self.min_heapify(smallest, attr_name)

    # constructs the minheap, time complexity = O(n)
    # attr_name is the attribute of the object that is stored in the heap
    def build_minheap(self, attr_name=None):
        # start from the last non-leaf index and go upto 1 and heapify at
        # each step
        for i in xrange(self.heap_size/2, 0, -1):
            self.min_heapify(i, attr_name)

    # returns the minimum element in the heap, time complexity = O(1)
    def get_min(self):
        return self.heap_list[1]

    # return the minimum from heap and also removes it, it returns None if
    # the heapsize if less than 1, time complexity = O(log2(n))
    def extract_min(self):
        # store the root somewhere, replace root with last element in heap and
        # heapify
        if self.heap_size < 1:
            print 'Heap Underflow'
            return None
        # extract min
        min_element = self.heap_list[1]
        # replace the minimum
        self.heap_list[1] = self.heap_list[self.heap_size]
        # now decrease the heap size
        self.heap_size -= 1
        # now heapify about the root, coz there might be disturbance in root
        self.min_heapify(1)
        # return minimum
        return min_element

    # increase the value at index passed in arg, time complexity = O(log2(n))
    def increase_key(self, index, value, attr_name=None):
        # check if new value is greater than previous value
        if value <= perform(self.heap_list[index], attr_name):
            print 'The new value', value, 'is less than value present there', \
                self.heap_list[index], 'kindly enter something proper\n'
            return False
        # set the value at given position
        self.heap_list[index] = value
        # as this is MinHeap and we've increased the value so there would be
        # no effect on the parent nodes, so we just need to heapify about the
        # index, so that all the nodes below index or at index get heapified
        self.min_heapify(index, attr_name)
        # returning True to indicate that increase has been done successfully
        return True

    # decrease the value at given index, time complexity = O(log2(n))
    def decrease_key(self, index, value, attr_name=None):
        # check passed value if lesser or not
        if value >= perform(self.heap_list[index], attr_name):
            print 'The new value', value, 'is greater than value present \
                there', self.heap_list[index], 'kindly enter a smaller value\n'
            return False
        # set the value
        self.heap_list[index] = value
        # as we have decreased the value so there might be effect on the parent
        # thus go to each parent and see if it satify minheap property
        while index > 1 and perform(self.heap_list[index/2], attr_name) > perform(self.heap_list[index], attr_name):
            # swap parent and child
            self.heap_list[index/2], self.heap_list[index] = \
                self.heap_list[index], self.heap_list[index/2]
            index /= 2
        # indicate that operation occurred successfully
        return True

    # insert the key in the heap, time complexity = O(log2(n))
    def insert_key(self, key, attr_name=None):
        # increase the heapsize
        self.heap_size += 1
        # put element there
        self.heap_list[self.heap_size] = key
        # get the last index
        index = self.heap_size
        # after the insertion the parent might get disturbed, so check for each
        # parent in the path to root
        while index > 1 and perform(self.heap_list[index/2], attr_name) > perform(self.heap_list[index], attr_name):
            # swap
            self.heap_list[index/2], self.heap_list[index] = \
                self.heap_list[index], self.heap_list[index/2]
            index /= 2


class MaxHeap(Heap):
    # constructor
    def __init__(self, heap_size=None, heap_list=None):
        Heap.__init__(self, heap_size, heap_list)

    # heapify the MaxHeap about the index passed as the argument
    # time complexity = O(log2(n))
    def max_heapify(self, i, attr_name=None):
        # step1: get the largest among left child, right child and root
        # step2: is largest is not the root, then swap and heapify for largest

        # get left index
        left = 2 * i
        # get right index
        right = 2 * i + 1

        # init the largest
        largest = -1

        # check the boundary for left also check if its greater or not
        if left <= self.heap_size and perform(self.heap_list[left], attr_name) > perform(self.heap_list[i], attr_name):
            largest = left
        else:
            largest = i

        # check the boundary for right also see if its greater than prev largest
        if right <= self.heap_size and \
                perform(self.heap_list[right], attr_name) > perform(self.heap_list[largest], attr_name):
            largest = right

        # step2: if root is not largest then you need to swap
        if largest != i:
            self.heap_li[largest], self.heap_li[i] = \
                self.heap_list[i], self.heap_list[largest]
            # there may be disordering in the child somewhere, so check them
            self.max_heapify(largest, attr_name)

    # constructs the MaxHeap, time complexity = O(n)
    def build_maxheap(self, attr_name=None):
        # start from the last non-leaf and go upto 1 and at each step
        # heapify
        for i in xrange(self.heap_size/2, 0, -1):
            self.max_heapify(i, attr_name)

    # returns the max from MaxHeap
    def get_max(self):
        return self.heap_list[1]

    # remove the maximum from heap and returns it
    # don't forget to check the return type while using this api
    # time complexity = O(log2(n))
    def extract_max(self):
        # store root in a var, then replace root with some element in heap
        # and heapify
        # check if heap has appropriate elements
        if self.heap_size < 1:
            print 'Heap Underflow'
            return None
        # extract maximum
        max_element = self.heap_list[1]
        # replace the root with last element in the heap
        self.heap_list[1] = self.heap_list[self.heap_size]
        # now decrease the heap_size
        self.heap_size -= 1
        # now heapify about the root
        self.max_heapify(1)
        # return element
        return max_element

    # increase the key at index passed in arg, time complexity = O(log2(n))
    def increase_key(self, index, value, attr_name=None):
        # check if the new value is greater then the previous key present in
        # heap or not
        if value <= perform(self.heap_list[index], attr_name):
            print 'The new value is less than element at', index,\
                ' kindly enter a greater value\n'
            return False
        # set the value at index
        self.heap_list[index] = value
        # as we have increased the value at index, so property of MaxHeap will
        # still be maintained, but check if the parent node is still MaxHeap
        # as chances are there that the increased value might be greater than
        # the parent of the node at position 'index'
        while index > 1 and perform(self.heap_list[index/2], attr_name) < perform(self.heap_list[index], attr_name):
            # swap parent and child
            self.heap_list[index], self.heap_list[index/2] = \
                self.heap_list[index/2], self.heap_list[index]
            # change the index to index/2
            index /= 2
        # returning True to indicate successful operation
        return True

    # decreases the value at position 'index'
    # time complexity = O(log2(n))
    def decrease_key(self, index, value, attr_name=None):
        # check if new value if lesser than previous value or not
        if value >= perform(self.heap_list[index], attr_name):
            print 'The new value is greater than element at', index,\
                ' kindly enter a lesser value than', self.heap_list[index], '\n'
            return False
        # set the value at position index
        self.heap_list[index] = value
        # in this case there is not chance that the parent node will
        # get disturbed, so just call the max_heapify for the node at index i
        self.max_heapify(index, attr_name)
        # returning True to indicate successful opreation
        return True

    # insert a key in MaxHeap, time complexity = O(log2(n))
    def insert_key(self, key, attr_name=None):
        # increase the size of heap
        self.heap_size += 1
        # put the element
        self.heap_list[self.heap_size] = key

        # get index
        index = self.heap_size

        # by the insertion the parent might get disturbed, so swap parent and
        # child if you find that parent node is smaller than the child
        while index > 1 and perform(self.heap_list[index/2], attr_name) < perform(self.heap_list[index], attr_name):
            # swap parent and child
            self.heap_list[index/2], self.heap_list[index] = \
                self.heap_list[index], self.heap_list[index/2]
            index /= 2
