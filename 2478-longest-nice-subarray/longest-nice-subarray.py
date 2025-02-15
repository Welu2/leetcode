class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0  # left pointer of the window
        current_and = 0  # bitwise AND of the current subarray
        max_len = 0  # store the length of the longest nice subarray

        for right in range(len(nums)):
            # If there is an overlap (common bits) between current subarray elements
            while (current_and & nums[right]) != 0:
                # Remove the leftmost element and update the AND value
                current_and ^= nums[left]
                left += 1

            # Add the current element to the subarray and update the AND
            current_and |= nums[right]
            # Update the maximum length
            max_len = max(max_len, right - left + 1)

        return max_len
