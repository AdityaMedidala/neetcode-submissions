class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        b=[]
        for i in range(len(nums)):
            difference=target-nums[i]
            if difference in a:
                b.append(a[difference])
                b.append(i)
            else:
                a[nums[i]]=i
        return b
                





       