class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        k=[]
        for i in s:
            if i not in k:
                k.append(i)
            else:
                l.append(len(k))
                idx=k.index(i)
                k=k[idx+1:]
                k.append(i)
        l.append(len(k))
        if l:
            return max(l)
        else:
            return 0