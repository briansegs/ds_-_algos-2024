# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones. 
# User defined class
class Node:
    def __init__(self, value): # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

# User defined class
class LinkedList: 
    def __init__(self, head): # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''
    def append(self, value):

        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next

        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)


    '''We will need this function to convert a LinkedList object into a Python list of integers'''
    def to_list(self):
        out = []          # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object

        while node:       # <-- Iterate untill we have nodes available
            out.append(int(str(node.value))) # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next

        return out


# My solution

def merge(list1, list2):
# TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''
    head = None
    l1 = list1.head
    l2 = list2.head

    while l1 and l2:
        if l1.value < l2.value:
            if head is None:
                head = l1
                tail = head
            else:
                tail.next = l1
                tail = tail.next
            l1 = l1.next
        else:
            if head is None:
                head = l2
                tail = head
            else:
                tail.next = l2
                tail = tail.next
            l2 = l2.next

    if l1:
        tail.next = l1

    if l2:
        tail.next = l2

    new_lst = LinkedList(head)
    return new_lst


''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''
class NestedLinkedList(LinkedList):
    def flatten(self):
        # TODO: Implement this method to flatten the linked list in ascending sorted order.
        new_lst = LinkedList(None)

        curr = self.head
        while curr.next:
            l1 = curr.value
            l2 = curr.next.value
            nxt = curr.next.next
            curr = Node(merge(l1, l2))
            curr.next = nxt

        new_lst.head = curr.value.head

        return new_lst

# First Test scenario
''' Create a simple LinkedList'''
linked_list = LinkedList(Node(1)) # <-- Notice that we are passing a Node made up of an integer
linked_list.append(3) # <-- Notice that we are passing a numerical value as an argument in the append() function here
linked_list.append(5)

''' Create another simple LinkedList'''
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)


''' Create a NESTED LinkedList, where each node will be a simple LinkedList in itself'''
nested_linked_list = NestedLinkedList(Node(linked_list)) # <-- Notice that we are passing a Node made up of a simple LinkedList object
nested_linked_list.append(second_linked_list) # <-- Notice that we are passing a LinkedList object in the append() function here

solution = nested_linked_list.flatten() # <-- returns A LinkedList object

expected_list = [1,2,3,4,5] # <-- Python list

# Convert the "solution" into a Python list and compare with another Python list
assert solution.to_list() == expected_list, f"list contents: {solution.to_list()}"
print("pass")

# My test

linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

''' Create another simple LinkedList'''
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)
''' And a third '''

third_linked_list = LinkedList(Node(2))
third_linked_list.append(4)

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
nested_linked_list.append(third_linked_list)

solution = nested_linked_list.flatten()

expected_list = [1,2,2,3,4,4,5]

# Convert the "solution" into a Python list and compare with another Python list
assert solution.to_list() == expected_list, f"list contents: {solution.to_list()}"
print("pass")
