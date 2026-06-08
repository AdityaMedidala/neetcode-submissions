class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        c=[]
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        sorted_a= dict(sorted(a.items(), key=lambda item:item[1],reverse=True))
        b=list(sorted_a.keys())
        for i in range(0,k):
            c.append(b[i])
        return c