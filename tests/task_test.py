import unittest
from src.task import task  # Correct import for the task class
from src.priority import priority  # Correct import for the priority enum

class TaskTest(unittest.TestCase):

    def setUp(self):
        # Create a task with some test values
        self.task = task(
            id=1,
            description="Initial Task",
            due_date="2024-09-30",
            priority=priority.NO_PRIORITY
        )
    
    def test_create_task(self):
        # Test initial values of the task
        self.assertEqual(self.task.id, 1)
        self.assertEqual(self.task.description, "Initial Task")
        self.assertEqual(self.task.due_date, "2024-09-30")
        self.assertEqual(self.task.priority, priority.NO_PRIORITY)
        self.assertFalse(self.task.completed)  # Task should be incomplete initially
    
    def test_task_updated(self):
        # Update description, due date, and priority
        self.task.update_description("Updated Task")
        self.task.update_due_date("2024-10-05")
        self.task.update_priority(priority.HIGH)
        
        # Test if the updates were applied correctly
        self.assertEqual(self.task.description, "Updated Task")
        self.assertEqual(self.task.due_date, "2024-10-05")
        self.assertEqual(self.task.priority, priority.HIGH)
    
    def test_marked_as_complete(self):
        # Mark task as complete
        self.task.mark_as_complete()
        
        # Test if the task is marked as completed
        self.assertTrue(self.task.completed)

if __name__ == '__main__':
    unittest.main()
