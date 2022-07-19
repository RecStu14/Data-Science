#PASCAL'S TRIANGLE

"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""
#done in 42ms
def generate_try1(numRows):
    pascal = []
    for i in range(0,numRows):
        if i == 0:
            pascal.append([1])
            
        elif i == 1:
            pascal.append([1,1])
            
        else:
            prevElement = pascal[-1]
            listSum = []
            
            for j in range(0,len(prevElement)-1):
                result = prevElement[j] + prevElement[j+1]
                listSum.append(result)
                   
            listSum.insert(0,1) #adding 1 to the front
            listSum.append(1) # adding 1 to the back
            pascal.append(listSum)
            
    return pascal


x = generate_try1(3)
print(x)


#done in 25ms  
def generate_try2(numRows):
    pascal = []
    
    def calc_sum(prevEle):
        listSum = []
        for j in range(0,len(prevEle)-1):
                result = prevEle[j] + prevEle[j+1]
                listSum.append(result)
        return listSum

    for i in range(0,numRows):
        if i == 0:
            pascal.append([1])
            
        elif i == 1:
            pascal.append([1,1])
            
        else:
            prevElement = pascal[-1]
            ans = calc_sum(prevElement)
                
            ans.insert(0,1) #adding 1 to the front
            ans.append(1) # adding 1 to the back
            pascal.append(ans) #adding the listSum to the final output list
        
            
    return pascal


y = generate_try2(3)
print(y)
                
                
                
                
            
            
            
        
        
        

