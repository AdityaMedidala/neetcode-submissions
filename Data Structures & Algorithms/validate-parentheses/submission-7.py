from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        a=deque()
        pair={
            '(':')',
            '[':']',
            '{':'}'
        }
        for i in s:
            if i in pair:
                a.append(i)
            else:
                if len(a)==0:
                    return False
                if pair[a[-1]]!=i:
                    return False
                a.pop()
        if len(a)==0:
            return True
        else:
            return False