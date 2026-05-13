class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for pos, speed in zip(position, speed):
            time = (target - pos) / speed
            cars.append((pos, time))
        
        cars.sort(reverse=True)
        
        count = 0
        curTime = 0
        for pos, time in cars:
            if time > curTime:
                count += 1
                curTime = time

        return count
        