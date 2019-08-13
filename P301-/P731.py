class MyCalendarTwo(object):

    def __init__(self):
        self.overlap = []
        self.all = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # compared with overlap:
        for (i, j) in self.overlap:
            if start < j and end > i:
                return False
        # add into self.all and .overlap
        for (i, j) in self.all:
            if start < j and end > i:
                self.overlap.append((max(start, i), min(end, j)))
        self.all.append((start, end))
        return True

if __name__ == '__main__':
# Your MyCalendarTwo object will be instantiated and called as such:
    MyCalendar = MyCalendarTwo()
    print(MyCalendar.book(10, 20))
    print(MyCalendar.book(50, 60))
    print(MyCalendar.book(10, 40))
    print(MyCalendar.book(5, 15))
    print(MyCalendar.book(5, 10))
    print(MyCalendar.book(25, 55))