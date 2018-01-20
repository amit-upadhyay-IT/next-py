'''
code to test the `dj_set_ll` module
'''
import dj_set_ll


if __name__ == '__main__':
    dj = dj_set_ll.DisjointSet(dict())
    dj.create_set('f')
    dj.create_set('g')
    dj.create_set('d')

    print dj.find_set('g').data  # g

    dj.create_set('c')
    dj.create_set('h')
    dj.create_set('e')
    dj.create_set('b')

    print dj.find_set('e').data  # e

    dj.union('f', 'g')
    dj.union('g', 'd')

    print dj.find_set('d').data  # f

    dj.union('f', 'c')
    dj.union('g', 'h')
    dj.union('f', 'e')
    dj.union('g', 'b')

    print dj.find_set('h').data  # f
    print dj.find_set('b').data  # f
