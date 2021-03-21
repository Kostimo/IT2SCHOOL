# Реализация с помощью котов и коробок

class Box:

    def __init__(self, cat):
        self.cat = cat
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    # Вставка узлов в начало списка
    def push(self, cat):
        newBox = Box(cat)
        newBox.next = self.head
        if self.head != None:
            self.head.prev = newBox
        self.head = newBox
        self.length += 1

lst = DoublyLinkedList()
lst.push("qwerty")
lst.push("lorem")
lst.push("ipsum")
# lst.insert(2, "amet")
# lst.insert(2, "end")
# lst.output(lst.head)