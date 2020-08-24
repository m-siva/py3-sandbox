
def twoSum(nums: [int], target:int):
    ans = {}  
    for i in range(len(nums)):
        tmp = target - nums[i]
        if tmp in ans:
            return [ans[tmp],i]
        ans[nums[i]] = i
    return

print(twoSum([1,2,3,4,5],4))