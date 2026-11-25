class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToName = {}
        emailGraph = defaultdict(list)

        for acc in accounts:
            name = acc[0]
            emails = acc[1:]

            for email in emails:
                emailToName[email] = name
                emailGraph[emails[0]].append(email)
                emailGraph[email].append(emails[0])
        
        seen = set()
        res = []

        def dfs(node, component):
            if node in seen:
                return
            seen.add(node)
            component.append(node)
            for nei in emailGraph[node]:
                dfs(nei, component)
        
        for email in emailToName:
            if email not in seen:
                component = []
                dfs(email, component)
                res.append([emailToName[email]] + sorted(component))
        return res
