from liner_list.linked_list.linked_list_tool import *
import sys


def reorder_list(head):
    """
    最后一组数据TLE了
    :param head:
    :return:
    """
    if head is None or head.next is None:
        return head
    t_head = head
    while t_head.next is not None:
        r_head = reverse_list(t_head.next)
        t_head.next = r_head
        t_head = t_head.next
    return head


def reorder_list_merge(head):
    if head is None or head.next is None:
        return head
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    mid = reverse_list(mid)  # 翻转后半部分链表
    head = merge_list(head, mid)
    return head


def merge_list(list1, list2):
    head = list1
    tail = head
    list1 = list1.next
    idx = 0
    while list1 is not None and list2 is not None:
        if idx % 2 == 0:
            tail.next = list2
            tail = tail.next
            list2 = list2.next
        else:
            tail.next = list1
            tail = tail.next
            list1 = list1.next
        idx += 1
    if list1 is not None:
        tail.next = list1
    if list2 is not None:
        tail.next = list2
    return head


def reverse_list(head):
    if head.next is None:
        return head
    current = None  # pre node
    while head is not None:
        tmp = head.next
        head.next = current
        current = head
        head = tmp
    return current


if __name__ == "__main__":
    line = sys.stdin.readline()
    head = create_linked_list(line)
    head = reorder_list_merge(head)
    print_linked_list(head)
