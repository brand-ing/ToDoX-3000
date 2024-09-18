import unittest
import taskmanager
from task import task
from priority import priority

# How do I know if the test passes or fails?
class taskmanager_test(unittest.TestCase):

    def setUp(self):
        self.task_manager = taskmanager.taskmanager()
        self.task = task(id=1, description="Task 1",due_date="2024-09-17",priority=priority.NO_PRIORITY)

    def test_add_task(self):
        self.task_manager.add_task(self.task)
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0].description, "Task 1")

    def test_complete_task(self):
        self.task_manager.add_task(self.task)
        self.task_manager.complete_task(1)
        self.assertTrue(self.task_manager.tasks[0].completed)

    def test_not_completed_task(self):
        self.task_manager.add_task(self.task)
        self.assertFalse(self.task.completed, "Newly created tasks should not be completed by default")

    def test_delete_task(self):
        self.task_manager.add_task(self.task)
        self.task_manager.delete_task(1)
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_update_task(self):
        self.task_manager.add_task(self.task)
        self.task_manager.update_task(1, new_description="Updated Task", new_due_date=None, new_priority=priority.MED)
        self.assertEqual(self.task_manager.tasks[0].description, "Updated Task")

    def test_search_tasks(self):
        self.task_manager.add_task(self.task)
        self.task_manager.add_task(task(2,"Another Task","2024-09-17",priority=priority.HIGH))
        results = self.task_manager.search_tasks("Another")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].description, "Another Task")

if __name__ == '__main__':
    unittest.main()

