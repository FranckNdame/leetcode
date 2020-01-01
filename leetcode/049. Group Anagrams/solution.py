def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_ = {}
        sortedStrs = ["".join(sorted(string)) for string in strs]

        for i in range(len(strs)):
            if sortedStrs[i] in hash_:
                hash_[sortedStrs[i]].append(strs[i])
            else:
                hash_[sortedStrs[i]] = [strs[i]]
                
            
        return list(hash_.values())