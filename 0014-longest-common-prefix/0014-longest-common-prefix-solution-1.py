class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ''

        prefix = strs[0]
        prefix_len = len(prefix)

        for i in range(1, len(strs), 1):
            s = strs[i]
            prefix_len = min(prefix_len, len(s))

            for j in range(prefix_len):
                if s[j] != prefix[j]:
                    prefix_len = j
                    break

            if prefix_len == 0:
                return ''

        return prefix[:prefix_len]
