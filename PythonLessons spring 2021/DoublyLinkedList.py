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
        if self.head is not None:
            self.head.prev = newBox
        self.head = newBox
        self.length += 1
    
    # Поиск узлов по индексу
    def index_search(self, index):
        counter = 0
        current = self.head
        while current is not None:
            if counter == index:
                return current
                break
            current = current.next
            counter += 1
        return f"The necessary cat is not on this list "

    # Поиск узлов по значению
    def value_search(self, cat):
        counter = 0
        current = self.head
        while current is not None:
            if current.cat == cat:
                return f"Cat \'{current.cat}\' has been found by index {counter}"
            current = current.next
            counter += 1
        return f"The necessary cat is not on this list "

    # Вставка узлов по индексу
    def insert(self, index_prevBox, cat):
        newBox = Box(cat)
        index = index_prevBox
        if index > self.length - 1:
            index = self.length - 1
        prevBox = self.index_search(index)
        newBox.next = prevBox.next
        prevBox.next = newBox
        newBox.prev = prevBox
        if newBox.next is not None:
            newBox.next.prev = newBox
        self.length += 1

    # Удаление узлов по индексу
    def remove(self, index):
        if index > self.length-1:
            print(f"The necessary cat is not on this list ")
            return
        box_to_delete = self.index_search(index)
        box_to_delete.prev.next = box_to_delete.next
        if box_to_delete.next is not None:
                    box_to_delete.next.prev = box_to_delete.prev
        box_to_delete.prev = None
        box_to_delete.next = None
        self.length -= 1

    # Вывод списка
    def output(self):
        print("----------")
        current = self.head
        while current is not None:
            print(current.cat)
            current = current.next
        print(f"Length: {self.length}.")

lst = DoublyLinkedList()
lst.push("qwerty")
lst.push("lorem")
lst.push("ipsum")
lst.insert(2, "sit")
lst.insert(7, "test1")
lst.remove(4)
lst.output()

