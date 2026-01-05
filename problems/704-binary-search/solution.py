class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Set up the boundaries for our search
        hi = len(nums) - 1
        lo = 0

        # Keep going as long as there's still a range to search
        while hi >= lo:
            # Find the middle point
            n = (hi + lo) // 2

            # Check if we found what we're looking for
            if nums[n] == target:
                return n

            # If the middle value is bigger than target, we can ignore the right half
            if nums[n] > target:
                hi = n - 1

            # Otherwise the target must be in the right half, so ignore left
            else:
                lo = n + 1

        # Didn't find it anywhere
        return -1
