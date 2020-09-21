class Solution(object):
    '''
    1052. Grumpy Bookstore Owner
    First scan the customer & grumpy array to calculate the number
    of total statisfied customers if the X minutes not applied.
    Then we just move the X-minutes window from the start, every
    time just need to recalculate based on previous window result
    and the value on the start & end of the sliding window. Also
    keep the maximum along the way.
    '''
    def maxSatisfied(self, customers, grumpy, X):
        # Get the number of satisfied customers
        # if the X minutes not applied
        total = 0
        for index in range(len(customers)):
            if grumpy[index] == 0:
                total += customers[index]

        result = total
        totalSatisfiedPrevWindow = total
        totalSatisfiedCurrentWindow = totalSatisfiedPrevWindow
        for end in range(len(customers)):
            start = end - X + 1
            if start > 0 and grumpy[start - 1] == 1:
                totalSatisfiedCurrentWindow -= customers[start - 1]
            if grumpy[end] == 1:
                totalSatisfiedCurrentWindow += customers[end]
            
            result = max(result, totalSatisfiedCurrentWindow)
            totalSatisfiedPrevWindow = totalSatisfiedCurrentWindow
            
        return result