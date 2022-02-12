# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def threeSum(self, nums):
        length = len(nums)
        nums.sort()
        result = []
        if length < 3:
            return []
        for i in range(0, length - 2):
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = length - 1
            while j != k:
                if j != i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                else:
                    if sum > 0:
                        k -= 1
                    else:
                        j += 1
        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.threeSum([0, 0, 0, 0]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
