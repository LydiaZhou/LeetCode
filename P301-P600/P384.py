import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        remaining = list(self.nums)
        returnVal = []
        for i in range(len(self.nums)):
            randomNum = random.randint(0, len(remaining) - 1)
            returnVal.append(remaining[randomNum])
            remaining.pop(randomNum)
        return returnVal

if __name__ == '__main__':
    # Your Solution object will be instantiated and called as such:
    obj = Solution([1,2,3])
    param_2 = obj.shuffle()
    print(param_2)
    param_1 = obj.reset()
    print(param_1)
    param_2 = obj.shuffle()
    print(param_2)
