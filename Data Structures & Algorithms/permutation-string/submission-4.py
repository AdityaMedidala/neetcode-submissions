class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=defaultdict(int)
        b=defaultdict(int)
        left=0
        right=len(s1)
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            a[s1[i]]+=1
            b[s2[i]]+=1
        while right<len(s2):
            if a==b:
                return True
            else:
                b[s2[left]]-=1
                if b[s2[left]]==0:
                    del b[s2[left]]
                left+=1
                b[s2[right]]+=1
                right+=1
        return a==b
