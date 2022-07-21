# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next'
def LLToList(l1):
    result = []
    while l1:
        result.append(l1.val)
        l1 = l1.next
        
    return result

def ListToLL(listname):
    root = ListNode(listname[0])
    current = root
    i = 1
    while (i<len(listname)):
        new_node = ListNode(val=listname[i])
        current.next = new_node
        i+= 1
        current = current.next
        
    return root

def iteration(list1):
    result = []
    for element in list1:
        result.append(element)
        
    return result

def checkElements(lists):
    size = len(lists)
    flag = False
    
    #If Empty False else True
    for element in lists:
        if element:
            flag = True
            break
        else:
            flag = False
            
    return flag
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        flag = checkElements(lists)
        if flag:
            all_results = []
            for linkedList in lists:
                current_list = LLToList(linkedList)
                results = iteration(current_list)
                all_results.extend(results)

            all_results.sort()

            ans = ListToLL(all_results)

        else:
            ans = ListNode(val="")
        return ans

            
        
        