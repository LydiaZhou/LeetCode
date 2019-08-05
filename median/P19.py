# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr = head
        dict = {}
        count = 0
        while ptr != None:
            dict[count] = ptr
            ptr = ptr.next
            count += 1
        # link
        if n == count:
            return head.next
        if n == 1:
            pre = dict[count - n - 1]
            pre.next = None
            return head
        pre = dict[count - n - 1]
        # toDelete = dict[count - n + 1]
        next = dict[count - n + 1]
        pre.next = next
        return head

    def removeNthFromEnd3(self, head, n):
        left = right = head
        for i in range(n):
            left = left.next
        if left == None:
            return head.next
        # move right to the one we'd like to delete
        while left.next != None:
            left = left.next
            right = right.next
        right.next = right.next.next
        return head

# REDO!!!!!
    def removeNthFromEnd(self, head, n):
        def backward(node):
            if node == None:
                return (0, node)
            (num, node.next) = backward(node.next)
            if num + 1 == n:
                return (num + 1, node.next)
            else:
                return (num + 1, node)
        # node.next = node.next.next
        return backward(head)[1]


if __name__ == '__main__':
    obj = Solution()
    obj = Solution()
    head = ListNode(1)
    tmp = head
    tmp.next = ListNode(2)
    tail = tmp.next
    tmp = tmp.next
    tmp.next = ListNode(3)
    tmp = tmp.next
    tmp.next = ListNode(4)
    tmp = tmp.next
    tmp.next = ListNode(5)
    print(obj.removeNthFromEnd(head, 2))
