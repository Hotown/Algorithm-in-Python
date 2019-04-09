from liner_list.linked_list.linked_list_tool import *
import sys
from heapq import heappop, heappush

def merge_k_lists(lists):
    if not list:
        return None

    trav = dummy = ListNode(-1)
    heap = []
    for i, ll in enumerate(lists):
        # 这里需要增加一个idx i
        # 因为遇到相同数据时，heapreplace_node先检查node.val发现相同，下一次比较node时是两个ListNode类型比较，会出错
        # 因此增加一位idx，避免比较到node
        if ll:
            heapreplace_node(heap, i, ll)
    print(heap)
    while heap:
        tuple_node = heappop(heap)
        idx = tuple_node[1]
        node = tuple_node[2]
        trav.next = node
        trav = trav.next
        if trav.next:
            heapreplace_node(heap, idx, trav.next)

    return dummy.next

def heapreplace_node(heap, i, node):
    heappush(heap, (node.val, i, node))