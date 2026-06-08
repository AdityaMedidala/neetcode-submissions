class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l1=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                    l1.append(i)
                    l1.append(j)
                    return l1
        