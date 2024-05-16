class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = defaultdict(int)
        maxlen, start = 0, 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                maxlen = max(maxlen, i - start+1)
            used[c] = i
        return maxlen