class Solution:
    def twosum(self, nums: list[int], target: int) -> list[int, int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(nums[i], nums[j])
        pass

    def twosums(self, nums: list[int], target: int) -> list[int, int]:

        for i, num in enumerate(nums):
            num_map = {}
            complacement = target - num
            if complacement in num_map:
                return (nums[complacement], i)
            num_map[num] = i




s1 = Solution()
s1.twosum([0, 1, 2, 3, 4, 5], 9)

nums = [0, 5, 2, 3, 9, 5]
