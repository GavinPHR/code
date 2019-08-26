# Partition to K Equal Sum Subsets
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) / k
        nums.sort(reverse=True)
        goodIdx = []
        def getSumIdx(left: int, curIdxs: [int], idx: int):
            if left == 0: return curIdxs
            if left < 0: return []
            while idx < len(nums) and nums[idx] > 0:
                tmp = list(curIdxs)
                tmp.append(idx)
                flag = getSumIdx(left - nums[idx], tmp, idx + 1)
                if flag:
                    goodIdx.append(flag)
                idx += 1
            return
        getSumIdx(target, [], 0)
        goodIdx = set(tuple(x) for x in goodIdx)
        print(goodIdx)
        def getK(current, curIdxs):
            if current == k: return True
            for s in goodIdx:
                flag = True
                for n in s:
                    if n in curIdxs:
                        flag = False
                        break
                if flag:
                    tmp = set(curIdxs)
                    tmp.update(s)
                    if getK(current + 1, tmp): return True
            return False
        a = set()
        return getK(0, a)

s = Solution()
print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))


