# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 일단 얘네 숫자로 바꿔야지
        n1 = 0
        p = 1
        while l1:
            n1 += l1.val*p
            p *= 10
            l1 = l1.next
        n2 = 0
        p = 1
        while l2:
            n2 += l2.val*p
            p *= 10
            l2 = l2.next
        total = n1 + n2

        # 이제 다시 리스트노드로 바꿀꺼임
        jjab1 = ListNode()
        jjab = jjab1
        
        if total == 0:
            return ListNode(0)
        while total > 0:
            solo = total % 10
            jjab.next = ListNode(solo)
            jjab = jjab.next
            total = total//10
        return jjab1.next
        