from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m=len(s)
        n=len(t)
        if m<n:
            return ""
        target=Counter(t)
        count=Counter()
        left=0
        right=0

        ans=""
        min_len=float("inf")

        while right<m:
            window=s[left:right+1]
            count[s[right]]+=1

            while count >=target:
                window_len=right-left+1
                if window_len<=min_len:
                    min_len=len(window)
                    ans=window
                count[s[left]]-=1
                if count[s[left]]==0:
                    del count[s[left]]
                left+=1
                window=s[left:right+1]
            right+=1
        return ans


