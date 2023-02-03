from Queue import Queue

def store_with_buffer(a_list, bandwidth):
    buffer = Queue()
    string = ""
    for i in a_list:
        for j in i:
            buffer.enqueue(j)
        if buffer.size() >= bandwidth:
            for i in range(bandwidth):
                string = string + buffer.dequeue()
        else:
            for i in range(buffer.size()):
                string = string + buffer.dequeue()
    print("Stored in the new string: " + string)
    print(f"Left in buffer: {buffer}")


list_of_data = ["010", "0110", "11001", "11"]
store_with_buffer(list_of_data, 3)

list_of_data = ["011001", "01110", "001", "0011", "11001", "0"]
store_with_buffer(list_of_data, 5)

list_of_data = ["010", "0110", "11001", "11"]
store_with_buffer(list_of_data, 2)