class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        
        wordSet = set(wordList)
        q = deque([beginWord])
        result = 0

        while q:
            result += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return result
                for i in range(len(node)):
                    for c in range(97, 123):
                        if node[i] == chr(c):
                            continue
                        n = node[:i] + chr(c) + node[i+1:]
                        if n in wordSet:
                            q.append(n)
                            wordSet.remove(n)
        return 0
        