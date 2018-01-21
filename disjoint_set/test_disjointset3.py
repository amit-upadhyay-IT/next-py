import disjointset3


if __name__ == '__main__':
    dj = disjointset3.DisjointSet(dict())
    dj.create_set('f')
    dj.create_set('g')
    dj.create_set('d')
    dj.create_set('c')
    dj.create_set('h')
    dj.create_set('e')
    dj.create_set('b')

    dj.union('f', 'g')
    print 'set of f: ', dj.find_set('f').data  # g
    dj.union('f', 'd')
    print 'set of d: ', dj.find_set('d').data  # g
    dj.union('f', 'c')
    dj.union('f', 'h')
    dj.union('f', 'e')
    dj.union('f', 'b')

    print 'set of h: ', dj.find_set('h').data  # f
    print 'set of b: ', dj.find_set('b').data  # f

    print '\nmember count'
    sets_list = dj.get_sets()
    for val in sets_list:
        print val.index_ptr.count
