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
        
        res = []
        seen = set()
        def dfs(node, emails):
            if node in seen:
                return
            seen.add(node)
            emails.append(node)
            for nei in emailGraph[node]:
                dfs(nei, emails)
        
        for email, name in emailToName.items():
            if email not in seen:
                emails = []
                dfs(email, emails)
                res.append([name] + sorted(emails))
        return res
        