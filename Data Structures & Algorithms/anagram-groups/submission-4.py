class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for i in strs:
            s=[0]*26
            for c in i:
                s[ord(c)-ord('a')] +=1
            a[tuple(s)].append(i)
        return list(a.values())




            