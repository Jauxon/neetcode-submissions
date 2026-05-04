class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #get all letters, val = str of all letters, key int = index of list
        groups = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - 97] += 1
            groups[tuple(counts)].append(s)

        return list(groups.values())

        
        
            

        
        