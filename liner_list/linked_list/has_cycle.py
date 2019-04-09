from liner_list.linked_list.linked_list_tool import *
import sys


def has_cycle(head):
    if head is None:
        return False
    slow = head
    fast = slow
    while True:
        if fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is None or slow is None:
                return False
            elif slow == fast:
                return True
        else:
            return False
    return False


if __name__ == '__main__':
    line = sys.stdin.readline()
    head = create_linked_list(line)
    print(has_cycle(head))
