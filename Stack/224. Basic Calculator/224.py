class Solution:
    '''
    224. Basic Calculator
    Stack
    '''
    def calculate(self, s: str) -> int:
        evaluate_stack = list()
        idx = 0
        while idx < len(s):
            if s[idx] == ' ':
                # ignore all the space
                idx += 1
                continue
            if s[idx] == '+' or s[idx] == '-' or s[idx] == '(':
                # for parenthesis and operators,
                # just push into stack
                evaluate_stack.append(s[idx])
                idx += 1
                continue
            if s[idx] >= '0' and s[idx] <= '9':
                # get the number in case it has
                # more than 1 digits
                num_str = ''
                while idx < len(s) and s[idx] >= '0' and s[idx] <= '9':
                    num_str += s[idx]
                    idx += 1
                num = int(num_str)
                if len(evaluate_stack) == 0 or evaluate_stack[-1] == '(':
                    # if stack empty or the top
                    # element is parenthesis, just
                    # push it into the stack
                    evaluate_stack.append(num)
                else:
                    # otherwise, the top element in
                    # the stack must be an operator,
                    # then we get the operator and
                    # the operand, evaluate it and
                    # push the result back to the 
                    # stack
                    operator = evaluate_stack.pop()
                    # this is to deal with negative number
                    left_operand = evaluate_stack.pop() if len(evaluate_stack) > 0 else 0
                    evaluate_stack.append((left_operand + num) if operator == '+' else (left_operand - num))
                continue
            if s[idx] == ')':
                # when we see right parenthesis, the top
                # element in the stack must be a number.
                # we just remove the left parenthesis
                # before that, before pushing the number
                # back in, we need to check if the top
                # element is now operator, to handle the
                # case like '··+(1+2)'
                num = evaluate_stack.pop()
                evaluate_stack.pop()
                if len(evaluate_stack) > 0 and evaluate_stack[-1] in ('+', '-'):
                    operator = evaluate_stack.pop()
                    left_operand = evaluate_stack.pop() if len(evaluate_stack) > 0 else 0
                    num = (left_operand + num) if operator == '+' else (left_operand - num)
                evaluate_stack.append(num)
                idx += 1

        # with the assumption that the input string is
        # an valid expression, the only number left in
        # the stack should just be the result
        return evaluate_stack[-1]