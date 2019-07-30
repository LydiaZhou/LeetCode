# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        oddTail = tmp = head
        # one step
        tmp = tmp.next
        if tmp == None:
            return head
        evenHead = evenTail = tmp
        tmp = tmp.next
        # loop
        count = 3
        while tmp != None:
            if count%2 == 1:
                oddTail.next = tmp
                oddTail = tmp
            else:
                evenTail.next = tmp
                evenTail = tmp
            tmp = tmp.next
            count += 1
        # attach the evenHead to oddTail
        oddTail.next = evenHead
        evenTail.next = None
        return head

if __name__ == '__main__':
    a = Solution()
    print(a.fractionToDecimal(-1, -2147483648))