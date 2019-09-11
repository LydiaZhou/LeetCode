class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: strx
        """
        # IPv4
        if "." in IP:
            nums = IP.split(".")
            if len(nums) != 4:
                return "Neither"
            for num in nums:
                if "0" > num or num >= "256" or len(num) > 3 or (num[0] == "0" and len(num) > 1):
                    return "Neither"
            return "IPv4"
        else:
            nums = IP.split(":")
            if len(nums) != 8:
                return "Neither"
            for num in nums:
                num = num.upper()
                if "0" > num or num >= "FFFF" or len(num) > 4:
                    return "Neither"
            return "IPv6"

if __name__ == '__main__':
    obj = Solution()
    print(obj.validIPAddress("172.16.254.1"))
    print(obj.validIPAddress("20EE:Fb8:85a3:0:0:8A2E:0370:7334"))
    print(obj.validIPAddress("256.256.256.256"))
