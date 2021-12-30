class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class Wordqueue:
    
    def __init__(self):
        self._first = None
        self._last = None
        
    def isEmpty(self):
        return self._first == None
    
    def enqueue(self, item):
        
        new_node = Node(item)
        if not self._first:
            self._first = new_node
        else:
            self._last.next = new_node
        self._last = new_node
    
    def size(self):
        current = self._first
        count = 0
        while current != None:
            count = count + 1
            current = current.next

        return count
    
    def peek(self):
        current = self._first
        if self._first == None:
            next_string = None
        else:
            next_string = current.data
        return next_string

    def look(self):
        current = self._first.next
        return current
    
    def dequeue(self):
        val = self._first.data
        self._first = self._first.next
        return val
    def overflow(self):
        output_text = ""
        current = self.first
        if current.data != ".":
            output_text = " "
        while current.data != ".":
            output_text = output_text + current.data
            current = current.next
        return output_text
    
    def __str__(self):
        return self._last.data



if __name__ == "__main__":

    q = LinkedQ()
    print(q.isEmpty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.size()


    x = q.dequeue()
    y = q.dequeue()
    z = q.dequeue()
    if (x == 1 and y == 2 and z == 3):
        print("OK")
    else:
        print("FAILED")
