import sys


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def create_linked_list(line):
    arr = [int(i) for i in line.split('->')]

    head = ListNode(None, None)
    tmp = head
    for data in arr[:-1]:
        node = ListNode(data, None)
        tmp.next = node
        tmp = node
    node = ListNode(arr[-1], None)
    tmp.next = node
    return head.next


def print_linked_list(head):
    while head.next != None:
        print('{:d}->'.format(head.val), end='')
        head = head.next
    print(head.val, end='')
