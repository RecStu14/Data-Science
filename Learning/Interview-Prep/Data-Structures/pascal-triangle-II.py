class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    
        def calc_sum(prevEle):
            listSum = []
            for j in range(0,len(prevEle)-1):
                    result = prevEle[j] + prevEle[j+1]
                    listSum.append(result)
            return listSum

        def generate(numRows):
            pascal = []

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

        pascalTriangle = generate(rowIndex+1)

        return pascalTriangle[-1]