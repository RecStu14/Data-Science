# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

#Node values are positive can work in terms of strings

def stringToLL(stringname):
    root = ListNode(val=stringname[0])
    current_node = root
    i = 1
    while (i < len(stringname)):
        new_node = ListNode(val=stringname[i])
        current_node.next = new_node
        i += 1
        current_node = current_node.next 
    return root

def LLToString(l1):
    string = ""
    while l1:
        string += str(l1.val)
        l1 = l1.next
    return string
    
        
    
class Solution:
    def reverseKGroup(self, head: [ListNode], k: int) -> Optional[ListNode]:
        string = LLToString(head)
        for i in range(0,1):
            rev = ""
            end = k + i
        
                
            for j in range(i,end):
                substring = string[i:k+i]
                if len(substring) == k:
                    rev += substring[::-1]
                    i += k
                    end = k + i
                    if end >= len(string):
                        end = len(string) -1   
                else:
                    break
                    
        
        tail = string[len(rev):]
        final_string = rev + tail
        
        ans = stringToLL(final_string)
        
        return ans
                
                

        
        