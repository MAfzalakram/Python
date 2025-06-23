def pairSum(nums, target):
    index = []
    i = 0
    j = len(nums) - 1
    while( i < j):
        if (nums[i] + nums[j]) > target:
            j -=1

        elif (nums[i] + nums[j]) < target:
            i +=1
        else:
            index.append(i)
            index.append(j)
            return index
    return index







nums = [1,2,4,6,7,9]
print(pairSum(nums,3))