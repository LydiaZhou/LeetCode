class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for str in strs:
            a = "".join(sorted(str))
            if a in dict:
                dict[a].append(str)
            else:
                dict[a] = [str]
        return dict.values()

if __name__ == '__main__':
    obj = Solution()
    print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

