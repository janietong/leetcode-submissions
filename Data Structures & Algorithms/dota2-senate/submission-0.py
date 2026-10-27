class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        rQueue = deque([i for i, val in enumerate(senate) if val == "R"])
        dQueue = deque([i for i, val in enumerate(senate) if val == "D"])
        n = len(senate)

        while rQueue and dQueue:
            ri = rQueue.popleft()
            di = dQueue.popleft()

            if ri < di:
                rQueue.append(ri + n)
            elif di < ri:
                dQueue.append(di + n)
        
        if rQueue:
            return "Radiant"
        return "Dire"

