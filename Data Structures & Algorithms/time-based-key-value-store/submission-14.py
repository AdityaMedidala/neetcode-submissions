class TimeMap:

    def __init__(self):
        self.a={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.a:
            self.a[key]=[[value,timestamp]]
        else:
            self.a[key].append([value,timestamp])
    def get(self, key: str, timestamp: int) -> str:
        if key in self.a:
            left=0
            right=len(self.a[key])-1
            self.candidate=[]
            while left<=right:
                mid=(left+right)//2
                if self.a[key][mid][1]<=timestamp:
                    self.candidate.append(self.a[key][mid][0])
                    left=mid+1
                elif self.a[key][mid][1]>timestamp:
                    right=mid-1
            if self.candidate:
                return self.candidate[-1]
            else:
                return ""
        return ""