class Solution(object):
    def partitionLabels(self, s):
        """
        :type S: str
        :rtype: List[int]
        """
        records = []
        for i in range(len(s)):
            if s[i] in records:
                records[s[i]] = (i, i)
            else:
                records[s[i]] = (record[s[i]][0], i)
        left = 0
        for record in records:


if __name__ == '__main__':
    obj = Solution()
    print(obj.partitionLabels("ababcbacadefegdehijhklij"))