#Works but is too slow when it comes to larger lists - 19999
def twoSum(nums, target):
    #find sum of remaining numbers with this number
    def findSum(nums, element, target, elementIndex):
        for j in range(0, len(nums)):
            ans = []
            if (j != elementIndex) and (element + nums[j] == target):
                ans.append(j)
                break
        return ans
            
    for i in range(0, len(nums)):
        element = nums[i]
        ans = findSum(nums, element, target, i)
        ans.append(i)
    return ans
    
        
#BEST Answer so far!
def twoSum_try2(nums, target):
    def calc_sum(nums, element, startIdx):
        result = []
        for j in range(startIdx, len(nums)):
            if element + nums[j] == target:
                result.append(startIdx-1)
                result.append(j)
                return result
            

    for i in range(0, len(nums)):
        element = nums[i]
        ans = calc_sum(nums, element, i+1)

        if ans != None:
             return ans
        
x = twoSum_try2([3,2,3],6)
print(x)

#This only works if the numbers are always beside each other!
def twoSum_try3(nums, target):
    result = []
    for i in range(0, len(nums)-1):
        if (nums[i] + nums[i+1] == target):
            result.append(i)
            result.append(i+1)
            break

    return result

#x = twoSum_try3([2,7,11,15], 9)
#print(x)




