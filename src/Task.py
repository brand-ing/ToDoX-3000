from Priority import Priority

class Task:

    def __init__(self, id, description, due_date=None, priority=Priority.NO_PRIORITY):
        self.id = id
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_as_complete(self):
        self.completed = True

    def update_description(self, new_description):
        self.description = new_description

    def update_due_date(new_due_date):
        self.due_date = new_due_date 

    def update_priority(self, new_priority):
        self.priority = new_priority


