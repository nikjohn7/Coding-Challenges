# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    prev_node = head
    if position == 0:
        new_node = SinglyLinkedListNode(data)
        new_node.next = head
        return new_node

    while prev_node is not None:
        new_node = SinglyLinkedListNode(data)

        for _ in range(position-1):
            prev_node = prev_node.next

        new_node.next = prev_node.next
        prev_node.next = new_node
        return head