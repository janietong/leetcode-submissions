class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def pick(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            even = (r - l) % 2 == 0
            left = piles[l] if even else 0
            right = piles[r] if even else 0
            dp[(l, r)] = max(left + pick(l + 1, r), right + pick(l, r-1))
            return dp[(l, r)]
        total = sum(piles)
        alice = pick(0, len(piles) - 1)
        return alice > total - alice
