from Node import Node

def create_linked_list(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            cur_node = head

            while cur_node.next:
                cur_node = cur_node.next

            cur_node.next = Node(value)

    return head


# Tests
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)



input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list(input_list)
test_function(input_list, head)
