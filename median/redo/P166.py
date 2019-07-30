class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator//denominator*denominator == numerator:
            return str(numerator//denominator)
        tuple = []
        tuple1 = []
        tuple2 = []
        if numerator < 0 and denominator < 0:
            resultStr = ""
            numerator = abs(numerator)
            denominator = abs(denominator)
        elif numerator < 0 or denominator < 0:
            resultStr = "-"
            numerator = abs(numerator)
            denominator = abs(denominator)
        else:
            resultStr = ""
        quotient = numerator // denominator
        resultStr += str(quotient) + "."

        remainder = numerator - denominator * quotient
        while remainder != 0:
            # Have ever met this one
            if remainder in tuple1:
                tuple2.append(quotient)
                startPoint = tuple1.index(remainder) + 1
                for i in range(1, len(tuple2)):
                    if i == startPoint:
                        resultStr += "("
                    resultStr += str(tuple2[i])
                return resultStr + ")"
            else:
                tuple1.append(remainder)
                tuple2.append(quotient)
            # loop
            quotient = remainder*10 // denominator
            remainder = remainder*10 - denominator * quotient

        if remainder == 0:
            for i in range(1, len(tuple2)):
                resultStr += str(tuple2[i])
            return resultStr + str(quotient)


if __name__ == '__main__':
    a = Solution()
    print(a.fractionToDecimal(-1, -2147483648))