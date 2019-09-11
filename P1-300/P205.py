class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        mappingSet = set()
        for i in range(len(s)):
            if s[i] in dict:
                if t[i] != dict[s[i]]:
                    return False
            else:
                if t[i] in mappingSet:
                    return False
                else:
                    mappingSet.add(t[i])
                    dict[s[i]] = t[i]
        return True

if __name__ == '__main__':
    obj = Solution()
    print(obj.isIsomorphic("egg", "add"))
    print(obj.isIsomorphic("foo", "bar"))
    print(obj.isIsomorphic("paper", "title"))
