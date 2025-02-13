"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.

"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the word at the end of a Trie path

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word  # Mark the end of the word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(node, r, c):
            char = board[r][c]
            if char not in node.children:
                return

            next_node = node.children[char]
            if next_node.word:  # If we reached a complete word
                found_words.add(next_node.word)
                next_node.word = None  # Avoid duplicate words in output

            board[r][c] = "#"  # Mark as visited

            # Explore neighbors: up, down, left, right
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in next_node.children:
                    dfs(next_node, nr, nc)

            board[r][c] = char  # Restore original character

            # Optimization: Remove leaf nodes to speed up future searches
            if not next_node.children:
                del node.children[char]

        # Build Trie from words
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        found_words = set()

        # Start DFS from each cell in the board
        for r in range(rows):
            for c in range(cols):
                dfs(trie.root, r, c)

        return list(found_words)
