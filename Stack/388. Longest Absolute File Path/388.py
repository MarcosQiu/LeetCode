class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split('\n')
        # stack, in format of (depth, length so far, dir_or_file_name)
        s = list()
        longest_len = 0
        for line in lines:
            splitted_line = line.split('\t')
            depth = len(splitted_line) - 1
            dir_file = splitted_line[-1]
            while len(s) > 0 and s[-1][0] >= depth:
                s.pop()
            if dir_file.find('.') != -1:
                # this is file
                longest_len = max(longest_len, len(dir_file) + 1 + (s[-1][1] if len(s) > 0 else -1))
            else:
                # this is dir
                s.append([
                    depth,
                    len(dir_file) + 1 + (s[-1][1] if len(s) > 0 else -1),
                    dir_file
                ])
        return longest_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt"))

