import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def div(a,b):
            return int(a/b)
        operators={"+":operator.add,
        "-":operator.sub,
        "*":operator.mul,
        "/":div
        }
        a=[]
        for i in tokens:
            if i in operators:
                op=operators[i]
                x=int(a.pop())
                y=int(a.pop())
                result=op(y,x)
                a.append(str(result))
            else:
                a.append(i)
        x=int(a[0])
        return x