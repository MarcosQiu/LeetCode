# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    24. Swap Nodes in Pairs
    Linked list
    '''
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_node = ListNode()
        dummy_node.next = head
        head = dummy_node

        current_node = dummy_node
        while (
            current_node is not None and
            current_node.next is not None and
            current_node.next.next is not None
        ):
            # at least there are 2 nodes after current_node,
            # and we need to perform a swap here
            first_node = current_node.next
            second_node = current_node.next.next
            current_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            current_node = first_node
        
        head = head.next
        return head