import itertools

class Solution(object):
    '''
    949. Largest Time for Given Digits
    Simple brute force version algorithm, both time & space complexity
    should be O(1) as there are always 24 possible combinations
    '''
    def largestTimeFromDigits(self, A):
        all_possible = list(itertools.permutations(A))
        valid_time = [x for x in all_possible if ((x[0] * 10 + x[1] < 24) and (x[2] * 10 + x[3] < 60))]
        
        if len(valid_time) == 0:
            return ''
        
        tmp = None
        chosen = None
        for candidate in valid_time:
            if chosen == None:
                tmp = self.toNumber(candidate)
                chosen = candidate
            else:
                if tmp < self.toNumber(candidate):
                    tmp = self.toNumber(candidate)
                    chosen = candidate
        return str(chosen[0]) + str(chosen[1]) + ':' + str(chosen[2]) + str(chosen[3])
                
    def toNumber(self, nums):
        return nums[0] * 1000 + nums[1] * 100 + nums[2] * 10 + nums[3]
    