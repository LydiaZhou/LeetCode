import itertools

class Solution(object):
    def braceExpansionII(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        level = 0
        groups = [[]]
        for i, char in enumerate(S):
            if char == "{":
                if level == 0:
                    start = i
                level += 1
            elif char == "}":
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(S[start + 1: i]))
            elif char == "," and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append(char)
        # convert groups to string
        wordSet = set()
        for group in groups:
            wordSet |= set(map(''.join, itertools.product(*group)))
        return sorted(wordSet)



if __name__ == '__main__':
    obj = Solution()
    print(obj.braceExpansionII("{c,{d,e},{f,k}}"))
    print(obj.braceExpansionII("{a,b}{c,{d,e}}"))
    print(obj.braceExpansionII("{{a,z},a{b,c},{ab,z}}"))
