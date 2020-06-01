import sys
sys.path.append('.dll')
from dll import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.oldest = None

    def append(self, item):
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.oldest = self.storage.head
            return

        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)

        elif self.storage.length == self.capacity:
            if self.oldest == self.storage.head:
                self.oldest.value = item
                self.oldest = self.oldest.next

            elif self.oldest == self.storage.tail:
                self.oldest.value = item
                self.oldest = self.storage.head

            else:
                self.oldest.value = item
                self.oldest = self.oldest.next
            
    def get(self):
        arr = []
        item = self.storage.head
        while item:
            arr.append(item.value)
            item = item.next
        return arr