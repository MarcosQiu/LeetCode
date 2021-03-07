class Solution:
	'''
	131. Palindrome Partitioning
	With DP + recursion
	'''
    def partition(self, s: str) -> List[List[str]]:
        str_len = len(s)
        is_palindrome = [[False] * str_len for _ in range(str_len)]

        # initialise the 2D array
        for idx in range(str_len):
            is_palindrome[idx][idx] = True
            if idx + 1 < str_len:
                is_palindrome[idx][idx + 1] = s[idx] == s[idx + 1]

        # Update the array in such an order
        # 0-2, 1-3, 2-4, ..., n-3-n-1
        # 0-3, 1-4, 2-5, ..., n-4-n-1
        # ...
        # ...
        # 0-n-1
        for length in range(3, str_len + 1):
            for idx in range(0, str_len - length + 1):
                start = idx
                end = idx + length - 1
                is_palindrome[start][end] = is_palindrome[start + 1][end - 1] and s[start] == s[end]

        return self.getPartitionWithMemo(s, 0, is_palindrome)

    
    def getPartitionWithMemo(self, s, cur_idx, is_palindrome):
        if cur_idx == len(s):
            return [[]]

        result = list()
        first_sub_string = ”“
        for end_idx in range(cur_idx, len(s)):
            first_sub_string += s[end_idx]
            # if the first substring is palindrome
            if is_palindrome[cur_idx][end_idx]:
                # recursively get palindrome sub-strings for the rest part
                tmp_results = self.getPartitionWithMemo(s, end_idx + 1, is_palindrome)
                for each in tmp_results:
                    result.append([first_sub_string] + each)

        return result
