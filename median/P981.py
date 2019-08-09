import collections

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dict[key].append((timestamp, value))


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.dict:
            return ""
        list = self.dict[key]
        left = 0
        right = len(list)
        if list[0][0] > timestamp:
            return ""
        elif list[right - 1][0] <= timestamp:
            return list[right - 1][1]
        # binary search
        while left < right - 1:
            mid = left + right // 2
            if list[mid][0] > timestamp:
                right = mid
            else:
                left = mid
        return list[left][1]


# Your TimeMap object will be instantiated and called as such:


if __name__ == '__main__':
    kv = TimeMap()
    kv.set("foo", "bar", 1)
    print(kv.get("foo", 1))
    print(kv.get("foo", 3))
    kv.set("foo", "bar2", 4)
    print(kv.get("foo", 4))
    print(kv.get("foo", 5))