# Problem Link: https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def oddEvenList(self, head: ListNode) -> ListNode:
            if head == None or head.next == None or head.next.next == None:
                return head
            root = head
            odd = head
            even = head.next
            evenstart = head.next
            while odd.next != None and even.next != None:
                odd.next = even.next
                odd = odd.next
                if odd != None:
                    even.next = odd.next
                    even = even.next  
            if even != None:
                even.next = None
            if odd == None:
                odd = evenstart
            else:
                odd.next = evenstart
            
            return root


                
        