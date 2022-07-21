# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Need to convert to lists and not strings cuz negative numbers involved

def ListToLL(l1):
    root = ListNode(val=l1[0])
    current_node = root
    i = 1
    while (i < len(l1)):
        new_node = ListNode(val=l1[i])
        current_node.next = new_node
        i += 1
        current_node = current_node.next
        
    return root

def LLToList(ll):
    result = []
    while ll:
        result.append(ll.val)
        ll = ll.next
    return result


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        l1 = LLToList(head)
        
        start_idx = left - 1
        
        #you dont -1 here cuz while splicing the last number is not included
        end_idx = right 
        
        sublist = l1[start_idx:end_idx]
        head = l1[:start_idx]
        tail = l1[end_idx:]
        
        rev_sublist = list(reversed(sublist))
        
        final_list = head + rev_sublist + tail
        
        ans = ListToLL(final_list)
        
        return ans
        