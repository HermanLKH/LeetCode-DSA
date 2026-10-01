class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefixes = []

        for c in strs[0]:
            prefixes.append(c)

        for s in strs[1::]:
            if prefixes:
                size_diff = len(prefixes) - len(s)

                if size_diff > 0:
                    for _ in range(0, size_diff, 1):
                        prefixes.pop()

                for i in range(0, len(prefixes), 1):
                    c = s[i]
                    
                    if c != prefixes[i]:
                        for _ in range(0, len(prefixes) - i, 1):
                            prefixes.pop()

                        break
            else:
                return ''

        return ''.join(prefixes)