class MinStack:
    """A stack that supports push, pop, top, and retrieving the minimum element in constant time."""

    def __init__(self):
        """Initializes an empty MinStack."""
        self.stack = []

    def push(self, val: int) -> None:
        """Pushes a value onto the stack and updates the current minimum.

        Args:
            val (int): The value to be pushed onto the stack.
        """
        min_num = self.getMin()
        min_num = val if min_num is None else min(min_num, val)
        self.stack.append([val, min_num])

    def pop(self) -> None:
        """Removes the element on the top of the stack."""
        self.stack.pop()

    def top(self) -> int:
        """Gets the top element of the stack.

        Returns:
            int: The value at the top of the stack.
        """
        return self.stack[-1][0]

    def getMin(self) -> int:
        """Retrieves the minimum element in the stack.

        Returns:
            int: The minimum element in the stack, or None if the stack is empty.
        """
        if self.stack == []:
            return None
        else:
            return self.stack[-1][1]
