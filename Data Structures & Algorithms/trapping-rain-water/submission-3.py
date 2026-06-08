class Solution:
    def trap(self, height: List[int]) -> int:
        left=[]
        right=[]
        x=0
        water=0
        for i in height:
            left.append(x)
            if i>=x:
                x=i
        y=0
        for i in reversed(height):
            right.append(y)
            if i>=y:
                y=i
        right.reverse()
        for i in range(len(height)):
            ans=min(left[i],right[i])-height[i]
            if ans>0:
                water+=ans
        return water
        
        