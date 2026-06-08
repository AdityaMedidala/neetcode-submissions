from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<=right:
            count=0
            k=(left+right)//2
            for i in piles:
                count+=ceil(i/k)
            if count<=h:
                right=k-1
            elif count>h:
                left=k+1
        return left
                