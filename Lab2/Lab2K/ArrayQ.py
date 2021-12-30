from array import array

class ArrayQ:
    def __init__(self):
        self.ary = array("i", [])

    def enqueue(self, integer):
        self.ary.append(integer)

    def dequeue(self):
        return self.ary.pop(0)

    def is_empty(self):
        return len(self.ary) == 0

if __name__ == "__main__":
    kortlek = [7, 1, 12, 2, 8, 3, 11,4, 9, 5, 13,6, 10]
    q = ArrayQ()

    for kort in kortlek:
        q.enqueue(kort)
    
    while True:
        if q.is_empty():
            break
        popped = q.dequeue()
        q.enqueue(popped)
        print(q.dequeue(), end = " ")

    # q.enqueue(1)
    # q.enqueue(2)
    # x = q.dequeue()
    # y = q.dequeue()
    # if (x == 1 and y == 2):
    #     print("OK")
    # else:
    #     print("FAILED")

# main()
