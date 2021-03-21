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

    # Вставка узлов по индексу
    def insert(self, index_prevBox, cat):
        newBox = Box(cat)
        counter = 0
        pointer = self.head
        while pointer != None:
            if counter == index_prevBox:
                newBox.next = pointer.next
                pointer.next = newBox
                newBox.prev = pointer
            if counter == index_prevBox + 2:
                pointer.prev = newBox
                break
            pointer = pointer.next
            counter += 1
        self.length += 1

    # Удаление узлов по индексу             ipsum lorem qwerty end amet
    def remove(self, index):
        counter = 0
        pointer = self.head
        while pointer.next != None:
            if counter + 1 == index:
                pointer.next = pointer.next.next
                if pointer.next != None:
                    pointer.next.prev = pointer
                break
            pointer = pointer.next
            counter += 1
        print(f"The necessary cat is not on this list ")
    
    # Поиск узлов по индексу
    def index_search(self, index):
        counter = 0
        pointer = self.head
        while pointer.next != None:
            if counter == index:
                return pointer.cat
                break
            pointer = pointer.next
            counter += 1
        return f"The necessary cat is not on this list "

    # Поиск узлов по значению
    def value_search(self, cat):
        counter = 0
        pointer = self.head
        while pointer.next != None:
            if pointer.cat == cat:
                return f"Cat \'{pointer.cat}\' has been found by index {counter}"
            pointer = pointer.next
            counter += 1
        return f"The necessary cat is not on this list "


    # Вывод списка
    def output(self, box):
        print("----------")
        while box != None:
            print(box.cat)
            box = box.next

lst = DoublyLinkedList()
lst.push("qwerty")
lst.push("lorem")
lst.push("ipsum")
lst.insert(2, "amet")
lst.insert(2, "end")
lst.output(lst.head)
lst.remove(3)
lst.output(lst.head)
lst.remove(3)
lst.output(lst.head)
lst.remove(3)
print(lst.index_search(0))
print(lst.index_search(-1))
print(lst.value_search("ipsum"))
print(lst.value_search("sit"))
