# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
            else:
                return True
        return False
