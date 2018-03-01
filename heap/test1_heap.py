import heap


class Unit(object):
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


def getUnitList(char_list, freq_list):
    unit_list = list()
    for i in xrange(len(char_list)):
        unit_list.append(Unit(char_list[i], freq_list[i]))
    return unit_list


def constructTree(minheap):
    while minheap.get_heap_size() > 1:
        z = Unit()
        print 'initial:',
        minheap.print_heap('freq')
        z.left = minheap.extract_min()
        print 'after one extract',
        minheap.print_heap('freq')
        z.right = minheap.extract_min()
        print 'after two extract',
        minheap.print_heap('freq')
        z.freq = z.left.freq + z.right.freq
        # print 'z.freq, z.char:', z.freq, z.char
        minheap.insert_key(z, 'freq')
        minheap.print_heap('freq')
    return minheap.get_min()


def print_tree(root, prefix):
    # base case
    if root.left is None and root.right is None and root.char.isalpha():
        print root.char, ':', prefix
        return
    print_tree(root.left, prefix+'0')
    print_tree(root.right, prefix+'1')


if __name__ == '__main__':
    char_list = ['f', 'e', 'c', 'b', 'd', 'a']
    freq_list = [5, 9, 12, 13, 16, 45]
    unit_list = getUnitList(char_list, freq_list)
    unit_list = ['empty'] + unit_list
    print [unit_list[i].char for i in xrange(1, len(unit_list))]
    minheap = heap.MinHeap(len(unit_list)-1, unit_list)
    minheap.build_minheap('freq')
    minheap.print_heap('char')
    print '---------------'
    root_node = constructTree(minheap)
    print root_node.left.left.left.char
    print_tree(root_node, '')
