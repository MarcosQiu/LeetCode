# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    92. Reverse Linked List II
    '''
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_node = ListNode(0, head)
        head = dummy_node
        first_list_head = head
        first_list_tail = None
        second_list_head = None
        second_list_tail = None
        third_list_head = None
        idx = 0
        current_node = head
        
        while idx <= right:
            if idx == left - 1:
                first_list_tail = current_node
                second_list_head = current_node.next
            if idx == right:
                second_list_tail = current_node
                third_list_head = current_node.next
            idx += 1
            current_node = current_node.next
        
        first_list_tail.next = None
        second_list_tail.next = None

        new_second_list_head, new_second_list_tail = self.reverse(second_list_head, second_list_tail)
        first_list_tail.next = new_second_list_head
        new_second_list_tail.next = third_list_head

        return head.next


    def reverse(self, head, tail):
        if head.next is None:
            return head, tail
        new_head, new_tail = self.reverse(head.next, tail)
        new_tail.next = head
        return new_head, head