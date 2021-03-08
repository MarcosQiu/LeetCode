class Solution:
    def minCut(self, s: str) -> int:
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

        minCuts = list(range(str_len))
        for idx in range(str_len):
            if is_palindrome[0][idx]:
                # if string s[0,..,idx] is palindrome, there
                # is no need to cut
                minCuts[idx] = 0
            else:
                # for the string s, one possible minimal cut is
                # the minimal cut s[0,..,i] + 1 given the condition
                # that s[i + 1,..,n - 1] is palindrome. To get the min
                # cut, just need to iterate i from 0 to n - 2, and
                # keep the minimal cut along the way 
                min_cut = minCuts[idx]
                for last_sub_string_start_idx in range(1, idx + 1):
                    if is_palindrome[last_sub_string_start_idx][idx]:
                        min_cut = min(
                            min_cut,
                            minCuts[last_sub_string_start_idx - 1] + 1
                        )
                minCuts[idx] = min_cut

        return minCuts[str_len - 1]