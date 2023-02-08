class Queue:
    def __init__(self):
        self.__items = []
    def is_empty(self):
        return self.__items == []
    def enqueue(self, item):
        self.__items.insert(0, item)                
    def dequeue(self):
        return self.__items.pop()
    def peek(self):
        return self.__items[len(self.__items) - 1]
    def size(self):
        return len(self.__items) 