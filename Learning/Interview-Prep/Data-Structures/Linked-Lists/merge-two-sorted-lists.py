# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def getLastNode(l1):
    last_node = l1
    while l1:
        last_node = l1
        l1 = l1.next
    return last_node

def LLToList(l1):
    elements = []
    while l1:
        elements.append(l1.val)
        l1 = l1.next
    return elements

def ListToLL(l1):

    root = ListNode(l1[0])
    current = root
    i = 1
    while (i<len(l1)):
        new_node = ListNode(l1[i])
        current.next = new_node
        i += 1
        current = current.next
    return root
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1:
            if list2:
                last_node_l1 = getLastNode(list1)
                last_node_l1.next = list2

                sorted_list = LLToList(list1)
                sorted_list.sort()
                ans = ListToLL(sorted_list)
                return ans
            else:
                return list1
        else:
            return list2

        
        
        
        