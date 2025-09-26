class WordDictionary:
    """
    A Word Dictionary implemented using a Trie data structure.
    Supports adding words and searching words, including with wildcard '.'.
    """

    def __init__(self):
        """
        Initialize the WordDictionary with an empty dictionary of children nodes
        and a flag to indicate the end of a word.
        """
        self.dict = {}
        self.flg = False

    def addWord(self, word: str) -> None:
        """
        Add a word to the WordDictionary.

        Args:
            word (str): The word to be added.

        Returns:
            None
        """
        trie = self
        for char in word:
            if char not in trie.dict:
                trie.dict[char] = WordDictionary()
            trie = trie.dict[char]
        trie.flg = True

    def search(self, word: str) -> bool:
        """
        Search for a word in the WordDictionary.
        The word may contain the wildcard character '.', which matches any single letter.

        Args:
            word (str): The word to search for, possibly including '.' as a wildcard.

        Returns:
            bool: True if the word exists in the WordDictionary, False otherwise.
        """
        if not word:
            return self.flg

        if word[0] == ".":
            for trie in self.dict.values():
                if trie.search(word[1:]):
                    return True

        if word[0] in self.dict:
            return self.dict[word[0]].search(word[1:])

        return False
