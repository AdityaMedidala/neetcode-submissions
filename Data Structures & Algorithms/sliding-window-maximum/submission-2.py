class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m=len(nums)
        left=0
        right=k-1
        l=[]
        while right<m:
            c=max(nums[left:right+1])
            l.append(c)
            left+=1
            right+=1
        return l


