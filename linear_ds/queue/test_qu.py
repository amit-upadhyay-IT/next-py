import qu


if __name__ == '__main__':
    queue = qu.Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    print 'front', queue.get_front()
    print 'rear', queue.get_rear()

    queue.dequeuq()
    print 'front', queue.get_front()
    print 'rear', queue.get_rear()
