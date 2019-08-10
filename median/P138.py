
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return
        dictRandom = {}
        newHead = Node(head.val, None, None)
        pre = newHead
        if head.random:
            randomVal = head.random.val
            dictRandom[randomVal] = [newHead]
        head = head.next
        while head != None:
            curNode = Node(head.val, None, None)
            pre.next = curNode
            if head.random:
                randomVal = head.random.val
                if randomVal in dictRandom:
                    dictRandom[randomVal].append(curNode)
                else:
                    dictRandom[randomVal] = [curNode]
            pre = curNode
            head = head.next
        # random puton
        tmpPtr = newHead
        while tmpPtr:
            if tmpPtr.val in dictRandom:
                for node in dictRandom[tmpPtr.val]:
                    node.random = tmpPtr
            tmpPtr = tmpPtr.next
        return newHead

if __name__ == '__main__':
    obj = Solution()
    n4 = Node(4, None, None)
    n3 = Node(3, n4, None)
    n2 = Node(2, n3, n3)
    n1 = Node(1, n2, n3)
    head = obj.copyRandomList(n1)
    print(1)

