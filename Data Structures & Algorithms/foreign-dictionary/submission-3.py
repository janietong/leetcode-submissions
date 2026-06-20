class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        d = {}
        for word in words:
            for c in word:
                d[c] = set()
        
        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    d[w1[j]].add(w2[j])
                    break

        result = []
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = True
            for nei in d[node]:
                if dfs(nei):
                    return True
            visited[node] = False
            result.append(node)
            return False

        for c in d:
            if dfs(c):
                return ""

        return "".join(reversed(result))      