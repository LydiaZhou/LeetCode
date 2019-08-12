# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return
        ptr = head.next
        ptr2 = head.next.next
        while ptr != ptr2 and ptr2 != None and ptr2.next != None:
            ptr = ptr.next
            ptr2 = ptr2.next.next
        if ptr != ptr2:
            return
        while ptr != head:
            ptr = ptr.next
            head = head.next
        return ptr


if __name__ == '__main__':
    obj = Solution()
    head = ListNode(3)
    tmp = head
    tmp.next = ListNode(2)
    tail = tmp.next
    tmp = tmp.next
    tmp.next = ListNode(0)
    tmp = tmp.next
    tmp.next = ListNode(-4)
    tmp = tmp.next
    tmp.next = tail

    print(obj.detectCycle(head))