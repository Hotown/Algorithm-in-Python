"""
Binary search in a reverse array.
[4,5,6,0,1,2] target = 0,
return 4
[4,5,6,0,1,2] target = 3,
return -1
"""
nums = [4, 5, 6, 0, 1, 2]
left, right = 0, len(nums) - 1
target = 3
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        print(mid)
        break
    if nums[left] > nums[right]:
        if nums[mid] < target:
            if target > nums[right]:
                left = mid + 1
            else:
                left = mid + 1
        else:
            if target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    else:
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
if left > right:
    print(-1)