class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        create = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in create:
                create[key] = [word]
            else:
                create[key].append(word)
        return list(create.values())