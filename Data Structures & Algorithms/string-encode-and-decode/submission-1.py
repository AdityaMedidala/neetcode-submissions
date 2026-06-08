class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in range(len(strs)):
            res+=str(len(strs[i]))+"#"+strs[i]
        return res



    def decode(self, s: str) -> List[str]:
        a=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            a.append(s[j+1:j+1+length])
            i=j+1+length
        return a