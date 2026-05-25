class Solution:
    def apply_operation(self,op , a, b):
        operation = {
            '+' : lambda a,b:a+b,
            '-' : lambda a,b:a-b,
            '/' : lambda a,b:a/b,
            '*' : lambda a,b:a*b,
        }
        return operation[op](int(a),int(b))

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for  i in range(len(tokens)):
            if tokens[i] in ['+' , '-' , '/' , '*']:
                top1 = stack.pop()
                top2 = stack.pop()
                val = self.apply_operation(tokens[i] , top2 , top1)
                stack.append(val)
            else:
                stack.append(tokens[i])
        return int(stack[0] )       




