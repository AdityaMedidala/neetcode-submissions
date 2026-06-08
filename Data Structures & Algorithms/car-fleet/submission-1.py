class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]
        for i in range(len(position)):
            x=target-position[i]
            time.append(x/speed[i])

        cars = sorted(zip(position, time), reverse=True)
        fleets = 0
        max_time = 0
        for pos, t in cars:
            if t > max_time:
                fleets += 1
                max_time = t
        
        return fleets