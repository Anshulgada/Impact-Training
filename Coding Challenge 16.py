from typing import List
from collections import defaultdict
class Solution:
    def getSignature(self, s: str) -> str:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        result = []
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])

        return ''.join(result)

    def groupAnagrams(self, n: int, mp: List[str]) -> int:
        groups = defaultdict(list)

        for s in mp:
            groups[self.getSignature(s)].append(s)

        return len(groups)

# Example usage:
solution = Solution()
n = int(input())
mp = [input() for _ in range(n)]
result = solution.groupAnagrams(n, mp)
print(result)