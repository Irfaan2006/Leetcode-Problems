class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        count = {}

        for char in t:
            count[char] = count.get(char, 0) + 1

        left = 0
        required = len(t)
        start = 0
        min_len = float("inf")

        for right in range(len(s)):
            if s[right] in count:
                if count[s[right]] > 0:
                    required -= 1

                count[s[right]] -= 1

            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                if s[left] in count:
                    count[s[left]] += 1

                    if count[s[left]] > 0:
                        required += 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]