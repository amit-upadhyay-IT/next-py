'''
code to test the `dj_set_ll` module
'''
import dj_set_ll


if __name__ == '__main__':
    dj = dj_set_ll.DisjointSet(dict())
    print 'creating set f\n'
    dj.create_set('f')
    print 'creating set g\n'
    dj.create_set('g')
    print 'creating set d\n'
    dj.create_set('d')

    print 'set of g: ', dj.find_set('g').data  # g

    print 'creating set c\n'
    dj.create_set('c')
    print 'creating set h\n'
    dj.create_set('h')
    print 'creating set e\n'
    dj.create_set('e')
    print 'creating set b\n'
    dj.create_set('b')

    print 'set of e: ', dj.find_set('e').data  # e

    print 'sets available'
    sets_list = dj.get_sets()
    for val in sets_list:
        print val.data

    print 'union of f and g\n'

    dj.union('f', 'g')

    print 'union of f and d\n'
    dj.union('f', 'd')

    print 'set of d: ', dj.find_set('d').data  # f

    print 'union of f and c\n'
    dj.union('f', 'c')
    print 'union of f and h\n'
    dj.union('f', 'h')
    print 'union of f and e\n'
    dj.union('f', 'e')
    print 'unipn of f and b\n'
    dj.union('f', 'b')

    print 'set of h: ', dj.find_set('h').data  # f
    print 'set of b: ', dj.find_set('b').data  # f

    print 'sets available\n'
    sets_list = dj.get_sets()
    for val in sets_list:
        print val.data
