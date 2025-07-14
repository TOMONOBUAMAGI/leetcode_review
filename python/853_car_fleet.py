from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """Calculates the number of car fleets that will arrive at the destination.

        A car fleet is a group of cars that travel together at the same speed
        because faster cars cannot pass slower ones once they meet.

        Args:
            target (int): The destination position all cars are moving toward.
            position (List[int]): The starting positions of the cars.
            speed (List[int]): The speeds of the cars.

        Returns:
            int: The number of car fleets that will arrive at the destination.

        Example:
            >>> sol = Solution()
            >>> sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
            3
        """
        if len(position) == 1:
            return 1

        cars = []
        for i in range(len(position)):
            cars.append([target - position[i], speed[i]])

        # Sort by how far each car has left to travel (i.e., position descending)
        cars = sorted(cars, key=lambda car: car[0])

        times_stack = []
        for car in cars:
            time = car[0] / car[1]
            if not times_stack or times_stack[-1] < time:
                times_stack.append(time)

        return len(times_stack)
