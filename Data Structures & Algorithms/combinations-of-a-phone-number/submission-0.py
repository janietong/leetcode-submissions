class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        d = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        result = []
        def dfs(i, curr):
            if i >= len(digits):
                result.append("".join(curr))
                return
            
            for let in d[int(digits[i])]:
                curr.append(let)
                dfs(i + 1, curr)
                curr.pop()
        
        dfs(0, [])
        return result
        


        