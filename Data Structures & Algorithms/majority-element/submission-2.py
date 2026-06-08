class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums1=defaultdict()
        for i in nums:
            nums1[i]=nums1.get(i,0)+1
        return(max(nums1, key=nums1.get))

