from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m=len(s)
        n=len(t)
        if m<n:
            return ""
        target=Counter(t)
        left=0
        right=0

        ans=""
        min_len=float("inf")

        while right<m:
            window=s[left:right+1]
            count=Counter(window)

            while count >=target:
                if len(window)<=min_len:
                    min_len=len(window)
                    ans=window
                left+=1
                window=s[left:right+1]
                count=Counter(window)

            right+=1
        return ans


