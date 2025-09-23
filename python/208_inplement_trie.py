class Trie:
    """
    A Trie (Prefix Tree) implementation for storing strings efficiently and
    supporting prefix-based queries.
    """

    def __init__(self):
        """
        Initialize the Trie with an empty node dictionary and a flag to mark the end of a word.
        """
        self.nodes = {}
        self.flg = False

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Args:
            word (str): The word to insert.

        Returns:
            None
        """
        trie = self
        for char in word:
            if char not in trie.nodes:
                trie.nodes[char] = Trie()
            trie = trie.nodes[char]
        trie.flg = True

    def search(self, word: str) -> bool:
        """
        Check if a word exists in the Trie.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word exists, False otherwise.
        """
        trie = self
        for char in word:
            if char not in trie.nodes:
                return False
            trie = trie.nodes[char]
        return trie.flg

    def startsWith(self, prefix: str) -> bool:
        """
        Check if there exists any word in the Trie that starts with the given prefix.

        Args:
            prefix (str): The prefix to check.

        Returns:
            bool: True if any word starts with the prefix, False otherwise.
        """
        trie = self
        for char in prefix:
            if char not in trie.nodes:
                return False
            trie = trie.nodes[char]
        return True
