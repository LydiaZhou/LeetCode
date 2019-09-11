import math

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        # get the list of all digits
        digits = []
        for char in time:
            if char.isdigit():
                digits.append(int(char))
        minDigit = min(digits)
        timeList = time.split(":")

        def finder(num, minLarger):
            for digit in digits:
                if digit > num and digit < minLarger:
                    minLarger = digit
            return minLarger

        # check the last digit of the Minute pointer
        minite0 = int(timeList[1][-1])
        minite0Replace = finder(minite0, 10)
        if minite0Replace != 10:
            return time[:-1] + str(minite0Replace)

        def finderTwo(num, minLarger):
            first = math.ceil(minLarger/10)
            for digit in digits:
                if digit > num//10 and digit < first:
                    first = digit
            if first == math.ceil(minLarger/10):
                return False
            return str(first) + str(minDigit)

        # check the first digit of the Minite pointer
        minute = int(timeList[1])
        minite1Replace = finderTwo(minute, 60)
        if minite1Replace:
            return timeList[0] + ":" + str(minite1Replace)

        # check the second digit of the Hour Pointer
        digitMax = 10
        if len(timeList[0]) == 2 and timeList[0][0] == '2':
            digitMax = 4
        hour0Replace = finder(int(timeList[0][-1]), digitMax)
        minMinute = str(minDigit) * 2
        if hour0Replace != digitMax:
            if len(timeList[0]) == 2:
                return timeList[0][0] + str(hour0Replace) + ":" + minMinute
            else:
                return '0' + str(hour0Replace) + ":" + minMinute

        # replace all
        return minMinute + ":" + minMinute

if __name__ == '__main__':
    obj = Solution()
    print(obj.nextClosestTime("22:37"))
    print(obj.nextClosestTime("14:39"))
    print(obj.nextClosestTime("10:59"))
    print(obj.nextClosestTime("23:59"))




