class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        map: dict[chr, 0] = {}
        map2: dict[chr, 0] = {}
        for i in s:
            if i in map:
                map[i] +=1
            else:
                map[i] = 1
        for i in t:
            if i in map2:
                map2[i] +=1
            else:
                map2[i] = 1
        if map == map2:
            return True
        return False
           
            
        
            
            


        