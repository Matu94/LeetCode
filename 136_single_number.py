nums = [4,1,2,1,2]

#Create a dictionary wich contains the nums and de apperances
count = {}
for num in nums:
    if num not in count:
        count[num] = 0
    count[num] += 1
        
#Check wich dict. element has the value '1'        
for key, value in count.items():
    if value == 1:
        return key