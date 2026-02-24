def is_monotonic(nums):
    """Method 1+7 hybrid: Two flags with early exit + direction awareness"""
    if len(nums) <= 1:
        return True
    if len(nums) == 2:
        return True

    direction = 0  # 0 = unknown, 1 = increasing, -1 = decreasing

    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            if direction == -1:
                return False
            direction = 1
        elif nums[i] > nums[i + 1]:
            if direction == 1:
                return False
            direction = -1
        # equal → no direction change

    return True

def is_strictly_monotonic(nums):
    """Strict version: no consecutive equals allowed after direction is set"""
    if len(nums) <= 1:
        return True

    direction = 0

    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            if direction == -1:
                return False
            if direction == 0:
                direction = 1
        elif nums[i] > nums[i + 1]:
            if direction == 1:
                return False
            if direction == 0:
                direction = -1
        else:  # equal
            if direction != 0:
                return False  # equals not allowed after direction set

    return True

# Method 2: all() – very clean
def is_monotonic_all(nums):
    if len(nums) <= 1:
        return True
    return (all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or
            all(nums[i] >= nums[i+1] for i in range(len(nums)-1)))

# Method 3: zip + slicing
def is_monotonic_zip(nums):
    if len(nums) <= 1:
        return True
    return (all(x <= y for x, y in zip(nums, nums[1:])) or
            all(x >= y for x, y in zip(nums, nums[1:])))

# Method 6: itertools.pairwise (Python 3.10+)
try:
    from itertools import pairwise
except ImportError:
    pairwise = None

def is_monotonic_pairwise(nums):
    if len(nums) <= 1:
        return True
    if pairwise is None:
        raise ImportError("pairwise requires Python 3.10+")
    return (all(x <= y for x, y in pairwise(nums)) or
            all(x >= y for x, y in pairwise(nums)))

# Method 5: NumPy version
try:
    import numpy as np
except ImportError:
    np = None

def is_monotonic_numpy(arr):
    if len(arr) <= 1:
        return True
    if np is None:
        raise ImportError("NumPy not installed")
    diff = np.diff(arr)
    return np.all(diff >= 0) or np.all(diff <= 0)
