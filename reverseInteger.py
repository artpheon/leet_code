#Given a signed 32-bit integer x,
#return x with its digits reversed.
#If reversing x causes the value to go outside
#the signed 32-bit integer range [-231, 231 - 1],
#then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        out = int(str(abs(x))[::-1])
        if (out <= 2**31):
            if x > 0 and out < 2**31:
                return out
            elif x < 0:
                return -out
            else:
                return 0
        else:
            return 0

sol = Solution()
print("Test case 1:" , sol.reverse(2147483647))
print("Test case 2:" , sol.reverse(0))
print("Test case 3:" , sol.reverse(1))
print("Test case 4:" , sol.reverse(-1))
print("Test case 5:" , sol.reverse(123))
print("Test case 6:" , sol.reverse(68745))
print("Test case 7:" , sol.reverse(+156))
print("Test case 8:" , sol.reverse(-100))
print("Test case 9:" , sol.reverse(-2147483648))
print("Test case 10:", sol.reverse(746384741))
print("Test case 11:", sol.reverse(-1463847412))