# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def LLToStr(l1):
            num = ""
            while l1:
                current = l1.val
                num += str(current)
                l1 = l1.next
            rev = num[::-1]
                
            return rev
        
        def stringToLL(result):
            string = result[::-1]
            string = list(map(int,string))

            root = ListNode(string[0])
            current = root
            i = 1
            while(i<len(string)):
                new_node = ListNode(val=string[i])
                current.next = new_node
                i+=1
                current = current.next
            return root
        
        l1_num = int(LLToStr(l1))
        l2_num = int(LLToStr(l2))
        
        result = str(l1_num + l2_num)
        
        ans = stringToLL(result)
        return ans
    
        
        
        
        
        
        
        
        
        
            
        
            
        
        
        
        
        
            
        
        
        
            
        
        