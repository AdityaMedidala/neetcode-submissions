class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=left
        a=defaultdict(int)
        res=0
        for right,i in enumerate(s):
            a[i]+=1
            length=right-left+1
            mode=max(a.values())
            x=length-mode
            while (x>k):
                a[s[left]]-=1
                left+=1
                length=right-left+1
                mode=max(a.values())
                x=length-mode
            res=max(res,length)
        return res

