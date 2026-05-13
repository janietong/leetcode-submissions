from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        rArr = []
        for v, t in self.d[key]:
            rArr.append(t)

        l = 0
        r = len(rArr) - 1
        rIdx = -1

        while l <= r:
            m = (l + r) // 2
            if rArr[m] <= timestamp:
                rIdx = m
                l = m + 1
            else:
                r = m - 1
        if rIdx == -1:
            return ""

        return self.d[key][rIdx][0]


        
