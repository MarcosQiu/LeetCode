class Solution:
    '''
    1047. Remove All Adjacent Duplicates In String
    Stack
    '''
    def removeDuplicates(self, S: str) -> str:
        stack = list()
        for ch in S:
            if len(stack) == 0 or ch != stack[-1]:
                # if stack is empty or current char
                # not the same as the one on top of
                # stack, just push it into the stack
                stack.append(ch)
            else:
                # otherwise, pop from stack and ignore
                # current char
                stack.pop()

        return ''.join(stack)