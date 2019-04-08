from liner_list.linked_list.linked_list_tool import *
import sys

def partition(head, x):
    if head is None:
        return head

    left, right = ListNode(0), ListNode(0)
    left_t, right_t = left, right
    while head is not None:
        if head.val < x:
            left_t.next = head
            left_t = head
        else:
            right_t.next = head
            right_t = head
        head = head.next
    right_t.next = None
    left_t.next = right.next
    return left.next


if __name__ == '__main__':
    line = sys.stdin.readline()
    head = create_linked_list(line)
    x = int(input())
    head = partition(head, x)
    print_linked_list(head)