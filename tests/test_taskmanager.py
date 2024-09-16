
import unittest
from src.TaskManager import TaskManager
from src.task import task

# How do I know if the test passes or fails?
class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        self.task_manager.add_task("Task 1", "2024-08-30")
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0].description, "Task 1")

    def test_complete_task(self):
        self.task_manager.add_task("Task 1")
        self.task_manager.complete_task(1)
        self.assertTrue(self.task_manager.tasks[0].completed)

    def test_delete_task(self):
        self.task_manager.add_task("Task 1")
        self.task_manager.delete_task(1)
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_update_task(self):
        self.task_manager.add_task("Task 1")
        self.task_manager.update_task(1, new_description="Updated Task")
        self.assertEqual(self.task_manager.tasks[0].description, "Updated Task")

    def test_search_tasks(self):
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Another Task")
        results = self.task_manager.search_tasks("Another")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].description, "Another Task")

if __name__ == '__main__':
    unittest.main()

