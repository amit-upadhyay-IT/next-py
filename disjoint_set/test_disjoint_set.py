import dj_set


if __name__ == '__main__':
    disjoint = dj_set.DisjointSet(dict())
    disjoint.create_set(10)
    disjoint.create_set(20)
    disjoint.create_set(30)
    disjoint.create_set(40)
    disjoint.create_set(60)
    disjoint.create_set(70)
    disjoint.create_set(80)
    disjoint.create_set(90)
    disjoint.create_set(150)

    disjoint.union(10, 20)
    disjoint.union(20, 30)
    disjoint.union(30, 60)

    print disjoint.find_set(20)
    print disjoint.find_set(10)
    print disjoint.find_set(30)
    print disjoint.find_set(60)

    print disjoint.find_set(150)

    disjoint.union(150, 10)
    print disjoint.find_set(150)
