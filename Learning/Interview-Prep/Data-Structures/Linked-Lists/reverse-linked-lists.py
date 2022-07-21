# TRY 1 - WORKS BUT NOT FULLY OPTIMIZED
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def LLToList(linkedlist):
    result = []
    while linkedlist:
        result.append(linkedlist.val)
        linkedlist = linkedlist.next
    return result

def ListToLL(listname):
    root = ListNode(val=listname[0])
    current_node = root
    i = 1
    while (i < len(listname)):
        new_node = ListNode(val=listname[i])
        current_node.next = new_node
        i += 1
        current_node = current_node.next
    return root


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(val="")
            
        if head:
            l1 = LLToList(head)
            rev_l1 = list(reversed(l1))
            ans = ListToLL(rev_l1)
        
           
        return ans
        

# TRY 2 - OPTIMIZED VERSION 
"""
Not very optimized in terms of time as it only improves by 1ms but the the memory improves significantly.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current_node = head
        
        while current_node:
            temp = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = temp
            
        return prev
            