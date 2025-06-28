class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        smaller_nums = []
        larger_nums = []
        just_half_count = 0

        half = target/2

        for num in nums:
            if num < half:
                smaller_nums.append(num)
            elif num == half:
                just_half_count += 1
            else:
                larger_nums.append(num)

        if just_half_count >= 2:
            half_indexes = [i for i, x in enumerate(nums) if x == half]
            return[half_indexes[0], half_indexes[1]]

        smaller_nums.sort()
        larger_nums.sort(reverse=True)

        for larger_num in larger_nums:
            for smaller_num in smaller_nums:
                sum = larger_num + smaller_num

                if sum == target:
                    return [nums.index(larger_num), nums.index(smaller_num)]
                elif sum > target:
                    break
