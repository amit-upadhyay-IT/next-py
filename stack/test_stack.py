import stack


if __name__ == '__main__':
    s = stack.Stack()
    s.push(50)
    s.push(40)
    s.push(30)
    s.push(20)
    print s.peek()
    s.pop()
    print s.peek()
