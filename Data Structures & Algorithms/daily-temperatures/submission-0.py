class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        b=[]
        n=len(temperatures)
        for i in range(len(temperatures)):
            count=i+1
            while count<n:
                if temperatures[count]>temperatures[i]:
                    b.append(count-i)
                    break
                else:
                    count+=1
            else:
                b.append(0)
        return b