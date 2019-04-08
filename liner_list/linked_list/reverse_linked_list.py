from liner_list.linked_list.linked_list_tool import *
import sys

def reverse(head):
    # write your code here
    current = None  # 记录前继节点
    while head != None:
        tmp = head.next
        head.next = current
        current = head
        head = tmp
    return current


if __name__ == '__main__':
    line = sys.stdin.readline()
    head = create_linked_list(line)
    head = reverse(head)
    print_linked_list(head)
