class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nn= {}
        for i, n in enumerate(nums):
            c = target - n
            if c in nn:
                return [nn[c], i]
            nn[n] = i