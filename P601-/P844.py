class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i = len(S) - 1
        j = len(T) - 1
        hashCountS = 0
        hashCountT = 0
        while i >= 0 and j >= 0:
            if S[i] == '#' or T[j] == '#':
                hashCountS += S[i] == '#'
                i -= S[i] == '#'
                hashCountT += T[j] == '#'
                j -= T[j] == '#'
                continue
            if hashCountS or hashCountT:
                i -= hashCountS > 0
                hashCountS -= (hashCountS > 0)
                j -= hashCountT > 0
                hashCountT -= (hashCountT > 0)
                continue
            if S[i] != T[j]:
                return False
            i -= 1
            j -= 1
        while i >= 0:
            if S[i] == '#':
                hashCountS += 1
            else:
                hashCountS -= 1
                if hashCountS < 0:
                    return False
            i -= 1
        while j >= 0:
            if T[j] == '#':
                hashCountT += 1
            else:
                hashCountT -= 1
                if hashCountT < 0:
                    return False
            j -= 1
        return True

if __name__ == '__main__':
    obj = Solution()
    print(obj.backspaceCompare("y#fo##f", "y#fx#o##f"))
    # print(obj.backspaceCompare("hd#dp#czsp#####", "hd#dp#czsp######"))




