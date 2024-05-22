from make_Linked_List_B import create_linked_list
from Node import Node

def mergeTwoLists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next

# Test
lst1 = [1, 2, 4]
lst2 = [1, 3, 4]
list1 = create_linked_list(lst1)
list2 = create_linked_list(lst2)

output = mergeTwoLists(list1, list2)
print("Should return: [1,1,2,3,4,4]")

curr = output
while curr:
    print(curr.value)
    curr = curr.next

lst1 = []
lst2 = []
list1 = create_linked_list(lst1)
list2 = create_linked_list(lst2)

output = mergeTwoLists(list1, list2)
print("Should return: []")

curr = output
while curr:
    print(curr.value)
    curr = curr.next

lst1 = []
lst2 = [3, 4]
list1 = create_linked_list(lst1)
list2 = create_linked_list(lst2)

output = mergeTwoLists(list1, list2)
print("Should return: [3,4]")

curr = output
while curr:
    print(curr.value)
    curr = curr.next
