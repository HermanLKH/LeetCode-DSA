class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        records = {}

        for s in magazine:
            records[s] = records.get(s, 0) + 1
        
        for s in ransomNote:
            if s in records and records[s] > 0:
                records[s] -= 1
            else:
                return False

        return True