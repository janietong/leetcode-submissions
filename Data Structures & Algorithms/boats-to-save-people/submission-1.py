class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0

        while l <= r:
            p1 = people[l]
            p2 = people[r]
            if p1 + p2 <= limit:
                res += 1
                l += 1
                r -= 1
            else:
                r -= 1
                res += 1
        return res 

