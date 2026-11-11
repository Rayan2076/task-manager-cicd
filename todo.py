class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.status = status
        self.completed = status == "Done"

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        sample_tasks = [
            Task("Create GitHub repository"),
            Task("Develop task manager"),
            Task("Write automated tests"),
            Task("Create Docker container"),
            Task("Configure CI workflow"),
            Task("Review workflow results"),
        ]

        for task in sample_tasks[:3]:
            task.mark_completed()

        self.tasks = sample_tasks

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]


def main():
    task_pool = TaskPool()
    task_pool.populate()

    print("Task Manager")
    print("============")

    print("\nToDo Tasks:")
    for task in task_pool.get_open_tasks():
        print(f"- {task.title}")

    print("\nDone Tasks:")
    for task in task_pool.get_done_tasks():
        print(f"- {task.title}")


if __name__ == "__main__":
    main()
