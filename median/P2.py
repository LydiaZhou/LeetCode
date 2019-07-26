# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addNumberCarry(self, l: ListNode, carry: int) -> ListNode:
        result = ListNode(-1)
        ptr = result
        while l != None:
            ptr.next = ListNode((carry + l.val)%10)
            carry = (carry + l.val) // 10
            ptr = ptr.next
            l = l.next
        if carry != 0:
            ptr.next = ListNode(carry)
        return result


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        start = 1
        while l1 != None and l2 != None:
            if start == 1:
                pointer = ListNode((l1.val + l2.val)%10)
                result = pointer
                start = 0
            else:
                pointer.next = ListNode((l1.val + l2.val + carry)%10)
                pointer = pointer.next
            carry = (l1.val + l2.val + carry)//10
            l1 = l1.next
            l2 = l2.next
        ## One of the linked list end
        remaining = ListNode(-1)
        if l1 != None:
            remaining = self.addNumberCarry(l1, carry)
        elif l2 != None:
            remaining = self.addNumberCarry(l2, carry)
        elif carry != 0:
            remaining.next = ListNode(carry)
        pointer.next = remaining.next
        return result

    def main(self):
        a = ListNode(3)
        a.next = ListNode(7)
        b = ListNode(9)
        b.next = ListNode(2)
        print(self.addTwoNumbers(a, b))

if __name__ == '__main__':
    a = Solution()
    a.main()