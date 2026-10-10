class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # s = "xyxxyzbzbbisl"
        # {x: [0, 3]}
        # {y: [1, 4]}
        # z: [5, 7]
        # b: [6, 9]
        # i: [10, 10]
        # s: [11, 11]
        # l: [12, 12]

        charToI = defaultdict(list)
        for i, c in enumerate(s):
            charToI[c].append(i)
        
        stack = []
        # stack = [[0, 4], [5, 9], [10, 10], [11, 11], [12, 12]]
        for idxs in charToI.values():
            start = idxs[0]
            end = idxs[-1]

            if not stack or stack[-1][1] < start:
                stack.append([start, end])
            else:
                stack[-1][1] = max(end, stack[-1][1])
        
        res = []

        for start, end in stack:
            res.append(end - start + 1)
        
        return res
        

