from liner_list.linked_list.linked_list_tool import *
import sys


def sort_list(head):
    if head is None or head.next is None:
        return head
    slow = head
    fast = slow

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    list1 = sort_list(head)
    list2 = sort_list(mid)

    sorted = merge(list1, list2)

    return sorted


def merge(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        t_head = list1
        list1 = list1.next
    else:
        t_head = list2
        list2 = list2.next

    tail = t_head

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            tail.next = list1
            tail = list1
            list1 = list1.next
        else:
            tail.next = list2
            tail = list2
            list2 = list2.next

    tail.next = list1 if list1 is not None else list2

    return t_head


if __name__ == '__main__':
    line = sys.stdin.readline()
    head = create_linked_list(line)
    sort_list(head)
    print_linked_list(head)
