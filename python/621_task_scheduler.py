from typing import List


class Solution:
    """
    Class to solve the Task Scheduler problem.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Calculate the least number of intervals required to finish all tasks
        with a cooldown period 'n' between the same tasks.

        Args:
            tasks (List[str]): List of task identifiers (single letters).
            n (int): Minimum cooldown period between same tasks.

        Returns:
            int: Minimum number of intervals needed to complete all tasks.
        """
        task_dic = {}
        for task in tasks:
            task_dic[task] = task_dic.get(task, 0) + 1

        max_num = max(task_dic.values())
        max_num_count = sum(1 for num in task_dic.values() if num == max_num)

        count = (n + 1) * (max_num - 1) + max_num_count

        return max(count, len(tasks))
