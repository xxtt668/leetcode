nums =[0,0,0]
nums.sort()
b = []
print(nums)
for i in range(1, len(nums)-1):
    print(i)
    j = 0
    m = len(nums) - 1
    while j != i and m != i:
        if (nums[j] + nums[i] + nums[m] == 0):
            b.append([nums[i], nums[j], nums[m]])
            while(nums[j]==nums[j+1] and j != i):
                j += 1
            while(nums[m]==nums[m-1] and m != i):
                m -= 1
        elif (nums[j] + nums[i] + nums[m] < 0):
            while (nums[j] == nums[j + 1]and j != i):
                j += 1
        elif (nums[j] + nums[i] + nums[m] > 0):
            while (nums[m] == nums[m - 1] and m != i):
                m -= 1
print(b)
