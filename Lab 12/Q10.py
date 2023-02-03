from Queue import Queue
def put_double_at_end(n, string):
    q = Queue()
    for letter in string:
        q.enqueue(letter)
    for i in range(n):
        q.enqueue(q.peek())
        q.enqueue(q.dequeue())
    new_string = ""
    while not q.is_empty():
        new_string = new_string + q.dequeue()
    return new_string
print(put_double_at_end(1,"a"))
print(put_double_at_end(1,"ab"))
print(put_double_at_end(0,"abc"))
print(put_double_at_end(1,"abc"))
print(put_double_at_end(2,"abc"))
print(put_double_at_end(3,"abc"))
