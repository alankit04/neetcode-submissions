class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group ={}

        for self in strs:
            key = ''.join(sorted(self))
            if key not in group:
                group[key] = []
            group[key].append(self)
        return list(group.values())
