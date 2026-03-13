
l1=[1,2,3,4,5,6]
target=5

def search(nums, target):
    print(nums)
    print(len(nums))
    middle = len(nums) // 2
    print(middle)
    if target < nums[middle] and len(nums) > 1:
        print('A')
        search(nums[0:middle], target)

    elif target > nums[middle] and len(nums) > 1:
        print('B')
        search(nums[middle:], target)

    else:
        print('C')
        print(nums[middle])
        return nums[middle]

x=search(l1,5)
print(x)