from Queue import Queue

def create_queue(string):
    q = Queue()
    for i in string.split(" "):
        q.enqueue(i)
    return q

def join_from_front(a_queue):
    string = ""
    for i in range(a_queue.size()):
        string = a_queue.dequeue() + string
    return string


q = create_queue('hello world')
print(join_from_front(q))
print(q.size())

q = create_queue('Python programming is fun')
print(join_from_front(q))