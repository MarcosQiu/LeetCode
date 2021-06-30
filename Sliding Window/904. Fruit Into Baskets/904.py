class Solution:
    def totalFruit(self, fruits):
        start_idx = 0
        last_appearance = dict()
        largest_fruits = 0
        for idx in range(len(fruits)):
            fruit = fruits[idx]
            if fruit not in last_appearance and len(last_appearance.keys()) == 2:
                largest_fruits = max(largest_fruits, idx - start_idx)
                fruit_to_remove = None
                for key in last_appearance.keys():
                    if last_appearance[key] == min(last_appearance.values()):
                        fruit_to_remove = key
                start_idx = last_appearance[fruit_to_remove] + 1
                del last_appearance[fruit_to_remove]
            last_appearance[fruit] = idx

        largest_fruits = max(largest_fruits, len(fruits) - start_idx)
        return largest_fruits


if __name__ == '__main__':
    s = Solution()
    print(s.totalFruit([0, 1, 2, 2]))
