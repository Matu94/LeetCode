nums = [3,2,4] #[2,7,11,15]
target = 6 #9

num_list = []
for index, num in enumerate(nums):
	if target - num in nums:
		num_list.append(index)

#https://www.code-recipe.com/post/two-sum
i = 0
j = i+1
for i in range(len(nums) - 1):
	for j in range(len(nums)):
		if nums[i] + nums[j] == target:
			if i != j:
				print()
				

#why dict : https://stackoverflow.com/questions/20372206/indexerror-list-assignment-index-out-of-range-in-python
seen = []
for index, num in enumerate(nums):

	remaining = target - nums[index]
	if remaining in seen:
		print(index, seen[remaining])

	seen[num] = index