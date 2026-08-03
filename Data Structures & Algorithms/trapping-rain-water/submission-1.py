class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(len(height) - 1):
            if i == 0:
                continue

            left_list = height[:i]
            right_list = height[i:]

            left_max = max(left_list)
            right_max = max(right_list)

            if height[i] >= right_max or height[i] >= left_max:
                continue

            trapped_water = min(left_max, right_max) - height[i]
            total = total + trapped_water

        return total