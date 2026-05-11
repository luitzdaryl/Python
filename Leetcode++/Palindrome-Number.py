'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

'''
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        reverse = 0 #initialization of the reverse  
        number = x #copy of the actual number

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x = x // 10

        return reverse == number
               
x = int(input("Enter the number: "))

solution = Solution()
print(solution.isPalindrome(x)) 