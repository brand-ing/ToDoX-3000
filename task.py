
class Task:

    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.due_date = None
        self.priority = None
        self.completed = False

    def mark_as_complete(self):
        self.completed = True

    def update_description(new_description):
        pass
    def update_due_date(new_due_date):
        pass
    def update_priority(new_priority):
        pass
