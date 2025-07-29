class TimeMap:
    """A time-based key-value store that can retrieve the value by key and timestamp.

    Supports setting a value for a given key and timestamp, and getting the value
    associated with a key at a particular timestamp or the closest timestamp before it.
    """

    def __init__(self):
        """Initializes the TimeMap with an empty dictionary."""
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Stores the key with the given value and timestamp.

        Args:
            key (str): The key to store.
            value (str): The value associated with the key.
            timestamp (int): The timestamp at which the value is stored.

        Example:
            >>> tm = TimeMap()
            >>> tm.set("foo", "bar", 1)
        """
        if key in self.data:
            self.data[key].append([timestamp, value])
        else:
            self.data[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        """Retrieves the value with the largest timestamp less than or equal to the given timestamp.

        Args:
            key (str): The key whose value should be retrieved.
            timestamp (int): The timestamp to search for.

        Returns:
            str: The value associated with the key at the given timestamp,
                or an empty string if no such timestamp exists.

        Example:
            >>> tm = TimeMap()
            >>> tm.set("foo", "bar", 1)
            >>> tm.get("foo", 1)
            'bar'
            >>> tm.get("foo", 0)
            ''
        """
        if key not in self.data:
            return ""

        res = ""
        left = 0
        right = len(self.data[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.data[key][mid][0] <= timestamp:
                res = self.data[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res
