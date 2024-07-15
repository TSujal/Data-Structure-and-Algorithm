
from typing import List

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) #{} #creating a dictionary
        result = []
        for word in strs:
            sorted_word = tuple(sorted(word))
            print(sorted_word)
            anagram_map[sorted_word].append(word)
        for value in anagram_map.values():
            result.append(value)

        return result

"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            hash_value = sum(ord(char) for char in word)
            if hash_value in anagram_map:
                anagram_map[hash_value].append(word)
            else:
                anagram_map[hash_value] = [word]
        return list(anagram_map.values())

"""
strs = ["abc","bac","cab","ad","bc"]
sol = Solution()
print(sol.groupAnagrams(strs))
