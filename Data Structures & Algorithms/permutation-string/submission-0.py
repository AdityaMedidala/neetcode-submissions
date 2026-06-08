class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=defaultdict(int)
        left=0
        right=len(s1)
        for i in s1:
            a[i]+=1
        while right>left and right<=len(s2):
            b=defaultdict(int)
            for x in s2[left:right]:
                b[x]+=1
            if a==b:
                return True
            else:
                left+=1
                right+=1
        return False


