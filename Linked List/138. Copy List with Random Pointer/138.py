# Definition for a Node.
class Node:
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        new_head = None
        prev_node = None
        current_node = head
        old_new_node_map = dict()
        while current_node is not None:
            node = Node(current_node.val, None, current_node)
            old_new_node_map[id(current_node)] = node
            if new_head is None:
                new_head = node
            if prev_node is not None:
                prev_node.next = node
            prev_node = node
            current_node = current_node.next

        current_node = new_head
        while current_node is not None:
            if current_node.random.random is not None:
                # if the origin node's random pointer is not None
                current_node.random = old_new_node_map[id(current_node.random.random)]
            else:
                current_node.random = None
            current_node = current_node.next

        return new_head


if __name__ == '__main__':
    five = Node(1)
    four = Node(10, five)
    three = Node(11, four)
    two = Node(13, three)
    one = Node(7, two)
    two.random = one
    three.random = five
    four.random = three
    five.random = one

    s = Solution()
    s.copyRandomList(one)
