"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None, count1=1, count2=0):
        self.value = value #name
        self.prev = prev
        self.next = next
        self.count1 = count1
        self.count2 = count2

    


    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

##########################################################################################3
"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length


    def insert(self, value):
        if not self.head:
            self.add_to_head(value)
            return

        current = self.head
        while current:
            if current.value == value:
                current.count1 +=1
                return
            else:
                current = current.next

        self.add_to_tail(value)
        return

    def insert2(self, value):
        if not self.head:
            self.add_to_head(value)
            return

        current = self.head
        while current:
            if current.value == value:
                current.count2 +=1
                return
            else:
                current = current.next

        self.add_to_tail2(value)
        return

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def remove_from_head(self):
        val = self.head.value
        self.delete(self.head)
        return val

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length+=1

        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def add_to_tail2(self, value):
        new_node = ListNode(value, None, None, 0, 1)
        self.length+=1

        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_from_tail(self):
        val = self.tail.value
        self.delete(self.tail)
        return val

    def move_to_front(self, node):
        # value = node.value
        # self.delete(node)
        # self.add_to_head(value)
        value = node.value
        if node == self.head:
            return
        if node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)

    def move_to_end(self, node):
        # value = node.value
        # self.delete(node)
        # self.add_to_tail(value)
        value = node.value
        if node == self.tail:
            return
        if node == self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

    def delete(self, node):
        self.length -= 1
        # if empty
        if not self.head:
            print('nothing doing')
            return

        # if just one node
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # at least two nodes and we want to delete the head
        elif node == self.head:
            self.head = node.next
            node.delete()

        #  we want to delete tail
        elif node == self.tail:
            self.tail = node.prev
            node.delete()     

        else:
            node.delete() # refers to method line 29

    def get_max(self):
        if not self.head:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            else:
                current = current.next
        return max_val