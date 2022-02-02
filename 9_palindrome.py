class Solution:
    def isPalindrome(self, x: int) -> bool:

        sx = str(x)


        end = len(sx) - 1
        value = []

        for i in range(len(sx)):
            if sx[i] == sx[end]:
                value.append(True)
            else:
                value.append(False)
            end = end -1

        result = all(element == True for element in value)
        return(result)