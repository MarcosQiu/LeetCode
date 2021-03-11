class Solution:
    '''
    227. Basic Calculator II
    Two stacks.
    '''
    def calculate(self, s: str) -> int:
        first_stack = list()
        idx = 0
        while idx < len(s):
            if s[idx] == ' ':
                # ignore all the spaces
                idx += 1
                continue
            if s[idx] >= '0' and s[idx] <= '9':
                # get the number if it has more
                # than one digit
                num_str = ''
                while idx < len(s) and s[idx] >= '0' and s[idx] <= '9':
                    num_str += s[idx]
                    idx += 1
                num = int(num_str)
                if len(first_stack) == 0 or first_stack[-1] in ('+', '-'):
                    # if it's either + or - on top 
                    # of the stack, just push it
                    # into the stack
                    first_stack.append(num)
                else:
                    # otherwise, evaluate and push the result
                    # back into the stack
                    operator = first_stack.pop()
                    left_operand = first_stack.pop()
                    first_stack.append(
                        left_operand * num if operator == '*' else left_operand // num
                    )
                continue
            # for all the operators, just
            # push it into the stack
            first_stack.append(s[idx])
            idx += 1

        # have the scond stack to handle all
        # the plus and minus calculation
        second_stack = list()
        for each in first_stack:
            if type(each) == int:
                if len(second_stack) == 0:
                    second_stack.append(each)
                else:
                    operator = second_stack.pop()
                    left_operand = second_stack.pop()
                    second_stack.append(
                        left_operand + each if operator == '+' else left_operand - each
                    )
            else:
                second_stack.append(each)
        
        return second_stack[0]
            