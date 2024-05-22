"Linked List"

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        while curr:
            if curr.val == index:
                return curr
            else:
                curr = curr.next

    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            dummy = Node(val)
            dummy.next = self.head
            self.head = dummy

    def insertTail(self, val: int) -> None:
        if self.tail is not None:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        prev = None
        while curr:
            if curr.val == index:
                prev.next = curr.next
                curr.next = None
                return
            else:
                prev = curr
                curr = curr.next


    def getValues(self):
        curr = self.head
        lst = []
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst

linkedList = LinkedList()
linkedList.insertHead(1)
linkedList.insertTail(2)
linkedList.insertHead(0)
linkedList.remove(1)
print("Should return: [0, 2]")
print(linkedList.getValues())
