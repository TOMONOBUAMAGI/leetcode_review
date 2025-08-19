class ListNode:
    """Doubly linked list node used in the LRU cache.

    Attributes:
        key (int): The key of the node.
        val (int): The value of the node.
        next (ListNode): Pointer to the next node in the list.
        prev (ListNode): Pointer to the previous node in the list.
    """

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    """Least Recently Used (LRU) Cache implementation.

    This class implements an LRU cache using a hash map for O(1) lookups
    and a doubly linked list to maintain the order of usage.

    Attributes:
        capacity (int): Maximum number of elements the cache can hold.
        dict (dict): Hash map to store key -> ListNode mappings.
        head (ListNode): Sentinel head node of the doubly linked list.
        tail (ListNode): Sentinel tail node of the doubly linked list.
    """

    def __init__(self, capacity: int):
        """Initialize the LRUCache with the given capacity.

        Args:
            capacity (int): Maximum number of elements the cache can hold.
        """
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.prev = self.tail
        self.tail.next = self.head

    def remove(self, node):
        """Remove a node from the doubly linked list.

        Args:
            node (ListNode): The node to remove.
        """
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        """Insert a node right before the head (most recently used position).

        Args:
            node (ListNode): The node to insert.
        """
        prev = self.head.prev
        node.prev = prev
        node.next = self.head
        self.head.prev = node
        prev.next = node

    def get(self, key: int) -> int:
        """Retrieve a value from the cache by key.

        If the key exists, the node is moved to the most recently used position.

        Args:
            key (int): The key to retrieve.

        Returns:
            int: The value associated with the key, or -1 if not found.
        """
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.insert(node)
            return self.dict[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        """Insert or update a key-value pair in the cache.

        If the cache exceeds its capacity, the least recently used item is evicted.

        Args:
            key (int): The key to insert or update.
            value (int): The value associated with the key.
        """
        if key in self.dict:
            self.remove(self.dict[key])
        self.dict[key] = ListNode(key, value)
        self.insert(self.dict[key])
        if len(self.dict) > self.capacity:
            del_node = self.tail.next
            del self.dict[del_node.key]
            self.remove(del_node)
