class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        y=self.stack.pop()
        return y

    def top(self) -> int:
        x=len(self.stack)-1
        return self.stack[x]
        

    def getMin(self) -> int:
        x=min(self.stack)
        return x
              
         
