class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        freq=[[] for i in range(len(nums)+1)]
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        for key,value in c.items():
            freq[value].append(key)
        res=[]
        for x in range(len(freq)-1,0,-1):
            for n in freq[x]:
                res.append(n)
                if len(res)==k:
                    return res