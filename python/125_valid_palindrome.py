class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Determines whether a given string is a valid palindrome, ignoring non-alphanumeric characters and case.

        A string is considered a palindrome if it reads the same forward and backward
        after converting to lowercase and removing all non-alphanumeric characters.

        Args:
            s (str): The input string to check.

        Returns:
            bool: True if the sanitized string is a palindrome, False otherwise.

        Example:
            >>> sol = Solution()
            >>> sol.isPalindrome("A man, a plan, a canal: Panama")
            True
            >>> sol.isPalindrome("race a car")
            False
        """
        if len(s) == 1:
            return True

        left = -1
        right = len(s)

        while left < right:
            left += 1
            right -= 1

            # Move left pointer to next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1

            # Move right pointer to previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

        return True
