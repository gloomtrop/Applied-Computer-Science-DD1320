class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None


class LinkedQ:
    
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
    
    def dequeue(self):
        val = self._first.data
        self._first = self._first.next
        return val



# q = LinkedQ()
# print(q.isEmpty())
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.size()


# x = q.dequeue()
# y = q.dequeue()
# z = q.dequeue()
# if (x == 1 and y == 2 and z == 3):
#     print("OK")
# else:
#     print("FAILED")