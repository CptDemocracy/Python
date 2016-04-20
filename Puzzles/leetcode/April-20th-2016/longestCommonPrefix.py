"""
[ref.href] leetcode.com/problems/longest-common-prefix
"
  Write a function to find the longest common prefix string amongst an array of strings.
"
"""
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ""
            
        # find the smallest string to potentially save time
        minlen = len(strs[0])
        for str in strs:
            currlen = len(str)
            if currlen < minlen:
                minlen = currlen
                
        # build a trie
        root = TrieNode('\0')
        for str in strs:
            node = root
            i = 0
            while i < minlen:
                c = str[i]
                if c not in node.children:
                    node.children[c] = TrieNode(c)
                node = node.children[c]
                i += 1
        
        # find the longest prefix
        prefix_chars = []
        
        node = root
        while len(node.children) == 1:
            next_char = node.children.keys()[0]
            node = node.children[next_char]
            prefix_chars.append(node.char)
            
        return "".join(prefix_chars)
