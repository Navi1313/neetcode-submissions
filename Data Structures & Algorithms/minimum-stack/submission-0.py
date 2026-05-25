class MinStack:

    def __init__(self):
        self.lis = []

    def push(self, val: int) -> None:
        if len(self.lis)== 0:
            self.lis.append([val , val])
        else:
            mini = self.lis[-1][1]
            mini = min(mini , val)
            self.lis.append([val , mini])

    def pop(self) -> None:
        if len(self.lis) == 0 :
            return

        return self.lis.pop() 


    def top(self) -> int:
        return self.lis[-1][0]
        

    def getMin(self) -> int:
        return self.lis[-1][1]
        
