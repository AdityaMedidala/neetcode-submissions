class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=[]
        b=set(numbers)
        for i in range(len(numbers)):
            difference=target-numbers[i]
            if difference in b:
                if difference != numbers[i] or (numbers.count(difference) > 1):
                    a.append(i+1)
        return a
