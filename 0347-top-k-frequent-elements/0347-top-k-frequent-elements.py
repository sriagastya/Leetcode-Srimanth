# Time Complexity: O(N*log(N))
# Space Complexity: O(N)
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = dict(Counter(nums))
        nums_count = sorted(nums_count)
        return nums_count[:k]
