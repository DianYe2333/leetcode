# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if (headA == None or headB == None):
            return None

        l = 0
        curA = headA
        curB = headB
        while (curA.next):
            l += 1
            curA = curA.next
        while (curB.next):
            l -= 1
            curB = curB.next

        if (not curA == curB):
            return None

        curA = headA if l > 0 else headB
        curB = headB if curA == headA else headA

        l = abs(l)
        while (l > 0):
            curA = curA.next
            l -= 1

        while (not curA == curB):
            curA = curA.next
            curB = curB.next

        return curA