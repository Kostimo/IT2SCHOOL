# Реализация с помощью котов и коробок

class Box:

    def __init__(self, cat):
        self.cat = cat
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # Добавление элементов в начало списка
    def push(self, cat):
        new_box = Box(cat, self.head, None)
        if self.head == None:
            self.head = new_box
        elif self.tail == None:
            self.tail = new_box
            self.head.prev = self.tail 
        else:
            self.head = self.tail
            self.tail = new_box
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length += 1


lst = DoublyLinkedList()
lst.push("qwerty")
lst.push("lorem")
lst.push("ipsum")
print(lst)