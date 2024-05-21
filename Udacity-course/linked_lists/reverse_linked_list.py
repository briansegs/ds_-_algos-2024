
from make_Linked_List_B import create_linked_list

def reverseList(head):
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


print("----")
lst = [1,2,3,4,5]
head = create_linked_list(lst)
rev_list = reverseList(head)

while rev_list:
    print(rev_list.value)
    rev_list = rev_list.next

print("----")
lst = []
head = create_linked_list(lst)
rev_list = reverseList(head)

while rev_list:
    print(rev_list.value)
    rev_list = rev_list.next

print("----")
lst = [1, 2]
head = create_linked_list(lst)
rev_list = reverseList(head)

while rev_list:
    print(rev_list.value)
    rev_list = rev_list.next
