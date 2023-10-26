from src.models.requests import EventRequest
from src.models.task import EventTask


class DataManager:
    event_request_dictionary = {}
    task_dictionary = {}

    # Event Request

    def add_event_request(self, newRequest):
        if isinstance(newRequest, EventRequest):
            self.event_request_dictionary[newRequest.record_number] = newRequest
        else:
            raise TypeError(
                "Error adding new event request ! Only EventRequest are allowed !"
            )

    def get_event_requests(self):
        return self.event_request_dictionary

    def get_event_request(self, record_number):
        if record_number in self.event_request_dictionary.keys():
            return self.event_request_dictionary[record_number]
        raise TypeError("Event request not found !")

    def delete_event_request(self, record_number):
        if record_number in self.event_request_dictionary.keys():
            del self.event_request_dictionary[record_number]
        else:
            raise TypeError("Event request not found !")

    # Task

    def add_task(self, newTask):
        if isinstance(newTask, EventTask):
            if newTask.project_reference in self.task_dictionary.keys():
                self.task_dictionary[newTask.project_reference].append(newTask)
            else:
                self.task_dictionary[newTask.project_reference] = [newTask]
        else:
            raise TypeError("Error adding new task ! Only EventTask are allowed !")

    def get_all_tasks(self):
        return self.task_dictionary

    def get_project_tasks(self, project_reference):
        if project_reference in self.task_dictionary.keys():
            return self.task_dictionary[project_reference]
        raise TypeError("Task not found !")

    def get_assignee_tasks(self, assigned_to):
        assignee_tasks = []
        for project_tasks in self.task_dictionary.values():
            assignee_tasks.extend(
                [task for task in project_tasks if task.assign_to == assigned_to]
            )
        if assignee_tasks:
            return assignee_tasks
        return "no_tasks"

    def delete_project_tasks(self, project_reference):
        if project_reference in self.task_dictionary.keys():
            del self.task_dictionary[project_reference]
        else:
            raise TypeError("Event request not found !")

    def delete_assignee_tasks(self, assigned_to):
        for project_ref, project_tasks in self.task_dictionary.items():
            self.task_dictionary[project_ref] = [
                task for task in project_tasks if task.assign_to != assigned_to
            ]
