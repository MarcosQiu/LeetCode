class Solution(object):
    '''
    1. Two Sum
    The idea is using dict to reduce running time, given the example
      nums = [2, 7, 11, 15], target = 9
    We just scan through the list, for the first number 2, we are
    looking for 7 (target - 2) in the rest of the array, so we save
    it to the mapping so that mapping[7] = 0. For each following number,
    we could check if it is one of the keys in the mapping. If that
    is the case, it means that this number, together with some number
    appears earlier (we can get the index from the dict value), sum up
    to the target we are given. 
    '''
    def twoSum(self, nums, target):
        mapping = dict()
        for index in range(len(nums)):
            if nums[index] in mapping:
                return [mapping[nums[index]], index]
            mapping[target - nums[index]] = index
            
        return []