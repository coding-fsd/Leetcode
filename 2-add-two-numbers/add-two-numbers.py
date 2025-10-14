# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        
        num1 = int("".join(map(str, list1[::-1])))
        num2 = int("".join(map(str, list2[::-1])))

        total = num1+num2
        total_str = str(total)[::-1]
        a = ListNode()
        d = a
        for ch in total_str:
            d.next = ListNode(int(ch))
            d = d.next
        return a.next
        
