class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=[]
        left=0
        right=len(numbers)-1
        for i in range(len(numbers)):
            sum1=numbers[left]+numbers[right]
            if sum1==target:
                a.append(left+1)
                a.append(right+1)
                return a
            elif sum1>target:
                right-=1
            elif sum1<target:
                left+=1
            