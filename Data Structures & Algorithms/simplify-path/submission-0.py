class Solution:
    def simplifyPath(self, path: str) -> str:
        i = 0
        n = len(path)
        stack = []

        for p in path.split("/"):
            if p == "" or p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)