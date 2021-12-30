from array import array

class Wordqueue:
    def __init__(self):
        self._items = array("i", [])

    def isEmpty(self):
        return self._items == array("i", [])

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

if __name__ == "__main__":
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("OK")
    else:
        print("FAILED")
        