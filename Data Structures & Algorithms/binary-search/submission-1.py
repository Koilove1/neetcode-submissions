class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0          # first index of the array
        right = len(nums) - 1         # last index of the array

        while left <= right:          # keep going while the range isn't empty
            mid = (left + right) // 2       # index halfway between left and right

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1  # target is to the RIGHT of mid, so cut off the left part
            else:
                right = mid - 1  # target is to the LEFT of mid, so cut off the right part

        return -1
