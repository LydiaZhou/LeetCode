class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        accountDict = {}
        for account in accounts:
            currentSet = set(account[1:])
            if account[0] in accountDict:
                currentEmails = accountDict[account[0]]
                existingNums = []
                for i in range(len(currentEmails)):
                    if (currentEmails[i] & currentSet):
                        existingNums.append(i)
                if len(existingNums) == 0:
                    accountDict[account[0]].append(currentSet)
                # elif len(existingNums) == 1:
                #     i = existingNums[0]
                #     currentSet = currentSet.union(currentEmails[i])
                #     accountDict[account[0]][i] = currentSet
                else:
                    for num in sorted(existingNums, reverse=True):
                        currentSet = currentSet.union(currentEmails[num])
                        accountDict[account[0]].pop(num)
                    accountDict[account[0]].append(currentSet)
            else:
                accountDict[account[0]] = [currentSet]
        # output
        output = []
        for (key, val) in accountDict.items():
            for ele in val:
                output.append([key] + sorted(list(ele)))
        return output

if __name__ == '__main__':
    obj = Solution()
    # print(obj.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))
    print(obj.accountsMerge([["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
     ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
     ["David", "David1@m.co", "David2@m.co"]]))