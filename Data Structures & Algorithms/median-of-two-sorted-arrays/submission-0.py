class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2

        nums.sort()
        m=len(nums)
        if m%2!=0:
            x=int(m/2)
            return nums[x]
        else:
            a=int(m/2)-1

            b=int(m/2)

            ans=(nums[a]+nums[b])/2
            return ans
