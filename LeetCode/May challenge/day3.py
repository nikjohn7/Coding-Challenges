class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if not i in magazine:
                return False
            magazine = magazine.replace(i, "", 1)
        return True