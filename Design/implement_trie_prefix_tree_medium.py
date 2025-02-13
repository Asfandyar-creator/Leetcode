"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        """Initialize the trie object."""
        self.root = TrieNode()
        
    def insert(self, word):
        """Inserts the string word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Returns true if the string word is in the trie, and false otherwise."""
        node = self._find_node(word)
        return node is not None and node.is_end_of_word
    
    def startsWith(self, prefix):
        """Returns true if there is a previously inserted string word that has the prefix."""
        return self._find_node(prefix) is not None
    
    def _find_node(self, prefix):
        """Helper function to traverse the Trie and return the last node of the prefix if exists."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

# Example usage:
# trie = Trie()
# trie.insert("apple")
# print(trie.search("apple"))  # True
# print(trie.search("app"))    # False
# print(trie.startsWith("app")) # True
# trie.insert("app")
# print(trie.search("app"))    # True
