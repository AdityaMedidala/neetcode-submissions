class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            a=[0]*26
            for b in i:
                a[ord(b)-ord("a")]+=1
            res[tuple(a)].append(i)
        return list(res.values())


            