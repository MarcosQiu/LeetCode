class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        last_planted_idx = -2
        for idx in range(len(flowerbed)):
            if flowerbed[idx] == 1:
                # if this plot is already planted
                last_planted_idx = idx
            elif (
                    idx - last_planted_idx > 1 and
                    (idx == len(flowerbed) - 1 or flowerbed[idx + 1] != 1)
            ):
                n -= 1
                last_planted_idx = idx

        return n <= 0

