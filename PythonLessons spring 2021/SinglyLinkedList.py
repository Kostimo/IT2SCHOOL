# Реализация с помощью котов и коробок

class Box:

    def __init__(self, cat, next):
        self.cat = cat
        self.next = next


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
    
    def insert(self, cat):
        self.head = Box(cat, self.head)
        self.length += 1
    
    def remove_at_index(self, index):
        dummy = Box(None, self.head)
        prev, curr = dummy, dummy.next
        counter = 0
        
        while curr:
            print(index, counter)
            if index == counter:
                prev.next = curr.next
                curr.next = None
            counter += 1
            prev, curr = curr, curr.next

    def iterate(self):
        box = self.head
        while(box):
            print(box.cat)
            box = box.next

    def search(self, cat):
        index = 0
        box = self.head
        while box:
            if box.cat == cat: 
                return index
            box = box.next
            index += 1
        return False