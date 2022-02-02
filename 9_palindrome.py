class Solution:
    def isPalindrome(self, x: int) -> bool:

        #x to string
        sx = str(x)

        #last index in string (-1 bcs len is start with 1, not 0)
        end = len(sx) - 1
        value = []


        for i in range(len(sx)):
            #check if the first and last index is the same then incerement/decrement
            #if true, add True to the list, else add False
            if sx[i] == sx[end]:
                value.append(True)
            else:
                value.append(False)

            #decrement end value ss
            end = end -1

        #check all elements in value, if all the same, result will be true
        result = all(element == True for element in value)
        return(result)