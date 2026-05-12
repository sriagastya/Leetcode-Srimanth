# Time Complexity: O(log26(N))
# Space Complexity: O(1)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ascii_start = 65
        result = ""
        while columnNumber:
            columnNumber -= 1
            current_num = columnNumber % 26
            current_char = chr(current_num + ascii_start)
            result = current_char + result
            columnNumber //= 26
        return result
