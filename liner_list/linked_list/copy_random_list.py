from liner_list.linked_list.linked_list_tool import *
import sys


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def copy_random_list(head):
    if head is None:
        return head
    dummy = RandomListNode(0)
    dummy.next = head
    table = dict()
    while head:
        table[head] = RandomListNode(head.label)
        head = head.next
    head = dummy.next
    while head:
        if head.next:
            table[head].next = table[head.next]
        if head.random:
            table[head].random = table[head.random]
        head = head.next

    start = RandomListNode(0)
    h = start
    head = dummy.next
    while head:
        h.next = table[head]
        h = h.next
        head = head.next

    return start.next
