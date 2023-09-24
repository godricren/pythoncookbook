from queueop import Queue

def joseph_problem(name_list,num):
    simqueue = Queue()
    for name in name_list:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()

print(joseph_problem(['Aaron', 'Bill', 'Candy', 'David', 'Emily','Frank', 'Green'],7))
