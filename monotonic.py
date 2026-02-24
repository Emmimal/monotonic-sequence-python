# Example: Best interview version (Method 7)
def is_monotonic(nums):
    """Check if sequence is monotonic (non-strict). O(n) time, O(1) space."""
    if len(nums) <= 2:
        return True
    direction = 0  # 0 = unknown, 1 = increasing, -1 = decreasing
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            if direction == 0:
                direction = 1
            elif direction == -1:
                return False
        elif nums[i] > nums[i + 1]:
            if direction == 0:
                direction = -1
            elif direction == 1:
                return False
    return True
