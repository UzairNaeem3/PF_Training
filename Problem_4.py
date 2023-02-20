from collections import deque
def lifo_queue():
    lifo = deque()
    print("LIFO QUEUE")
    while True:
        len = input("Please enter the length of the queue: ")
        if len.isdigit():
            for i in range(int(len)):
                lifo.appendleft(input(f"Please enter anything at index {i+1}: "))
                print(f"Your given Queue: {lifo}")
        else:
            print("Please enter the length in positive integers.")
            continue
        break
    print("------------Extracting Elements from Queue------------")
    while True:
        extract = input("How much elements you want to get? ")
        if extract.isdigit():
            if extract > len:
                print("Please enter a smaller number than the length of the Queue.")
                continue
            else:
                for i in range(int(extract)):
                    print(lifo.popleft(),end=' ')
        else:
            print("Please enter the length in positive integers.")
            continue
        break
    print(f"\nRemaining elements in Queue: {lifo}")

lifo_queue()
