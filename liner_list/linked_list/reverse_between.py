from liner_list.linked_list.linked_list_tool import *
import sys


def reverse(head):
    current = None
    while head != None:
        tmp = head.next
        head.next = current
        current = head
        head = tmp
    return current

def reverse_between(head, m, n):
    head_node = ListNode(-1, head)
    mth_pre = find_kth(head_node, m - 1)
    mth = mth_pre.next
    nth = find_kth(head_node, n)
    nth_next = nth.next
    nth.next = None

    reverse(mth)
    mth_pre.next = nth
    mth.next = nth_next
    return head_node.next

def find_kth(head, k):
    for i in range(k):
        if head is None:
            return None
        head = head.next
    return head

if __name__ == '__main__':
    line = sys.stdin.readline()
    head = create_linked_list(line)
    m = int(input())
    n = int(input())
    head = reverse_between(head, m, n)
    print_linked_list(head)

