"""
Question: 2 PALINDROME NUMBER
Given an integer x, return true if x is a palindrome and false otherwise.

Example 1: Input: X = 121
Output = True
Explanation : 121 read as 121 from left and right and from right and left.


Constraints:
* -2^31 <= x <= 2^31 - 1

"""

class Solution:
    def isPalindrome(self,x: int) -> bool:
        if x<0: return False
        div = 1
        while x >= 10*div:
            div = div*10
        while x:
            right = x % 10 #getting the right digit
            left = x // div # getting the left most digits
            if left != right:
                return False

            #chooping the right and left digit
            x = (x%div) // 10
            div = div/100
        return True



if __name__ == '__main__':
    solution = Solution() #making an object of the class
    x = 10
    print(solution.isPalindrome(x))