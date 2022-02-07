nums = [1, 3, 5, 6]
target = 5        

'''
for num in nums:
    if target == num:
        return(nums.index(target))
        break
    else:
        if num > target:
            return(nums.index(num))
            break
        else:
            return(len(nums))
'''

'''
if target in nums:
    return nums.index(target)
else:
    for num in nums:
        if num > target:
            return(nums.index(num))
        else:
            return(len(nums))
'''

if target in nums:
    print(nums.index(target))
else:
    for index, num in enumerate(nums):
        if num > target:
            print(nums.index(num))
        if (index + 1) == len(nums):
            print(len(nums))