class Solution(object):
    '''
    1004. Max Consecutive Ones III
    Basic idea is having two pointers, covering subarray that it
    contains at most K 0s. When moving the right pointer, moving
    left pointer as well so that at most K 0s are included.
    '''
    def longestOnes(self, A, K):
        head = 0
        tail = -1
        zeroCount = 0
        # initial state setup
        while tail < len(A) - 1:
            if A[tail + 1] == 1:
                tail += 1
            else:
                if zeroCount < K:
                    zeroCount += 1
                    tail += 1
                else:
                    break
        maxLen = max(0, tail - head + 1)

        while head < len(A) - 1 and tail < len(A) - 1:
            if A[head] == 0:
                zeroCount -= 1
                while tail < len(A) - 1:
                    if A[tail + 1] == 1:
                        tail += 1
                    else:
                        if zeroCount < K:
                            zeroCount += 1
                            tail += 1
                        else:
                            break
            head += 1
            maxLen = max(maxLen, tail - head + 1)

        return maxLen

    '''
    This is a clear version with the same idea from
    https://leetcode.com/problems/max-consecutive-ones-iii/discuss/853856/Python-or-O(N)-or-Beats-80
    '''
    def longestOnesClearVersion(self, A, K):
        maxones = 0
        start = 0
        zeroes = 0
        
        for end in range(len(A)):
            if A[end] == 0:
                zeroes += 1
            
            while zeroes > K:
                if A[start] == 0:
                    zeroes -= 1
                start += 1
            
            maxones = max(maxones, end-start+1)
        
        return maxones
