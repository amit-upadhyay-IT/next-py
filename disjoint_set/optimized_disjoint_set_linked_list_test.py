import optimized_disjoint_set_linked_list


if __name__ == '__main__':
    dj = optimized_disjoint_set_linked_list.DisjointSet(dict())
    dj.create_set('f')
    dj.create_set('g')
    dj.create_set('d')
    dj.create_set('c')
    dj.create_set('h')
    dj.create_set('e')
    dj.create_set('b')

    dj.union('f', 'g')
    dj.union('f', 'd')
    dj.union('f', 'c')
    dj.union('f', 'h')
    dj.union('f', 'e')
    dj.union('f', 'b')

    print 'set of h: ', dj.find_set('h').data  # f
    print 'set of b: ', dj.find_set('b').data  # f

    print 'member count\n'
    sets_list = dj.get_sets()
    print sets_list[0].index_ptr.count
