from operator import add, sub, mul, floordiv
'''
150. Evaluate Reverse Polish Notation
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        opMap = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": floordiv
        }
        for el in tokens:
            if el not in opMap:
                stack.append(int(el))
            else:
                right_operand = stack.pop()
                left_operand = stack.pop()
                op = opMap[el]
                res = op(left_operand, right_operand)
                if el == '/' and left_operand % right_operand !=0 and res < 0:
                    res += 1
                stack.append(res)

        return stack[0]