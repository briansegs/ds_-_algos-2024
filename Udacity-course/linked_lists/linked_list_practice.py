class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    if self.head is None:
        self.head = Node(value)
    else:
        node = Node(value)
        node.next = self.head
        self.head = node


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
linked_list.prepend(2)
linked_list.prepend(3)
assert linked_list.to_list() == [3, 2, 1], f"list contents: {linked_list.to_list()}"
print("Pass")

# append

def append(self, value):
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here    
    if self.head is None:
        self.head = Node(value)
    else:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(value)

LinkedList.append = append

# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 3, 2, 1, 3], f"list contents: {linked_list.to_list()}"
print("pass")

# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"
print("pass")

def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    curr = self.head
    while curr:
        if curr.value == value:
            return curr
        else:
            curr = curr.next
    return False

LinkedList.search = search

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"
print("pass")

# remove

def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    curr = self.head
    dummy = Node(0)
    dummy.next = curr
    prev = dummy
    while curr:
        if curr.value == value:
            prev.next = curr.next
            break
        else:
            prev = curr
            curr = curr.next
    self.head = dummy.next

LinkedList.remove = remove

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"
print("pass")

# pop

def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    if self.head:
        value = self.head.value 
        self.head = self.head.next
        return value
    return None

LinkedList.pop = pop

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"
print('pass')

# insert

def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """

    # TODO: Write function to insert here    
    curr_pos = 0
    curr = self.head
    dummy = Node(0)
    dummy.next = curr
    prev = dummy
    while curr:
        if curr_pos == pos:
            prev.next = Node(value)
            prev.next.next = curr
            break
        elif curr.next is None:
            curr.next = Node(value)
            break
        else:
            prev = curr
            curr = curr.next
            curr_pos += 1
    self.head = dummy.next

LinkedList.insert = insert

# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
print("pass")

# Size

def size(self):
    """ Return the size or length of the linked list. """
    # TODO: Write function to get size here
    count = 0
    curr = self.head
    while curr:
        curr = curr.next
        count += 1

    return count

LinkedList.size = size

# Test size function
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"
print("pass")
