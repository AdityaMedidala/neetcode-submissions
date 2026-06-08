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
            for i in reversed(self.a[key]):
                if i[1]<=timestamp:
                    return i[0]
            return ""
        else:
            return ""
