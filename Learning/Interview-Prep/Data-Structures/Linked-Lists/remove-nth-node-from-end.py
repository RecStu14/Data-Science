# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def llToList(head):
        elements = []
        while head:
            elements.append(head.val)
            head = head.next

        return elements
        
def ListToLl(final_list):
    root = ListNode(final_list[0])
    current_node = root
    i = 1
    while (i<len(final_list)):
        new_node = ListNode(final_list[i])
        current_node.next = new_node
        i+=1
        current_node = current_node.next
    return root
            
class Solution:
            
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        org = head
        
        elements = llToList(head)
        rev_elements = list(reversed(elements))
        
        del rev_elements[n-1]
        
        final_list = list(reversed(rev_elements))
        
        if final_list:
            ans = ListToLl(final_list)
        else:
            ans = ListNode(val="")
            
        
        return ans
        
    
            
            
            
        
        
            
        
    
            
        
                
            
        
        
            
        
        
        