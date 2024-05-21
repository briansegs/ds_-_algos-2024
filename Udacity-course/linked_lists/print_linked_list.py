from make_Linked_List_B import create_linked_list



def print_linked_list(head):
    cur = head
    while cur:
        print(cur.value)
        cur = cur.next

# Test
# lst = [3, 5, "hi", "fire", 10]
# head = create_linked_list(lst)
# print_linked_list(head)
