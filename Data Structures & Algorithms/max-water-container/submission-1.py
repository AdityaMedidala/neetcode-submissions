class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        water=0
        while j>i:
            x=min(heights[i],heights[j])*(j-i)
            if x > water:
                water = x
            if heights[j]>heights[i]:
                i+=1
            else:
                j-=1
        return water



        