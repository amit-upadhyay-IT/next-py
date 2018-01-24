qu.py gives the utility methods for working with queue. However you don't need to import anything for working with basic queues in python bcoz `list()` in python can be used for that purpose.

Example:
```py
queue = list()

# to add use:
queue.append(data)  # going to be inserted at end

# to pop use:
queue.pop(0)  # going to be removed from beginning
```

However if you want to use queue in multithreaded programming then you should be using [this](https://docs.python.org/2/library/queue.html).
