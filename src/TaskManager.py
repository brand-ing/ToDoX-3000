
import json


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self,description, due_date, priority):
        task.id = len(self.tasks) + 1
        new_task = Task(task_id, description, due_date, priority)
        self.tasks.append(new_task)
        
    def list_tasks(self):
        for task in tasks:
            print(f"Description: {task.description}, Due: {task.due_date}, Priority: {task.priority}, Completed: {task.completed}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_as_complete()
                print(f"SUCCESS: Task marked as completed.")
                #TODO Add to a completed items list

        print(f"Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"Task has been deleted.")
                return
        print(f"Task not found.")

    def update_task(self, task_id, new_description, new_due_date):
        for task in self.tasks:
            if task.id == task_id:
                if new_description:
                    task.update_description(new_description)
                if new_due_date:
                    task.update_due_date(new_due_date)
                if new_priority:
                    task.update_priority(new_priority)
                print(f"Task updated.")
                return
        print(f"Task not found.")

    def search_tasks(self, keyword):
        found_tasks = []
        for task in self.tasks:
            if keyword.lower() in task.description.lower():
                found_tasks.append(task)
        return found_tasks

    def save_tasks(filename):
        task_data = []
        for task in self.tasks:
            task_dict = {
                'id': task.id,
                'description': task.description,
                'due_data': task.due_date,
                'priority': task.priority if task.priority != Priority.NO_PRIORITY else None,
                'completed': task.completed
            }
            task_data.append(task_dict)

            with open(filename, 'w') as file:
                json.dump(tasks_data, file, indent=4)
            print(f"Tasks saved to {filename}")

    def load_tasks(filename):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                
            for task_dict in tasks_data:
                task = Task(
                    id=task_dict['id'],
                    description=task_dict['description'],
                    due_date=task_dict['due_date'],
                    priority=Priority[task_dict['priority']] if task_dict['priority'] else None
                )
                task.completed = task_dict['completed']
                self.tasks.append(task)
            
            print(f"Tasks loaded from {filename}")
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {filename}.")
