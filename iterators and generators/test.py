
nums = [0,0,1,1,1,2,2,3,3,4]

print(list(set(nums)) + ['_'] * (len(nums) - len(set(nums))))