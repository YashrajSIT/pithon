def count_occurrences(nums, target):
    def find_position(nums, target, find_first):
        left, right = 0, len(nums) - 1
        position = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                position = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return position

    start = find_position(nums, target, True)
    if start == -1:
        return 0  # target not found
    end = find_position(nums, target, False)
    
    return end - start + 1

# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = int(input("enter the no="))
print(count_occurrences(nums, target))  # Output: 2

target = int(input("enter the no="))
print(count_occurrences(nums, target))  # Output: 0