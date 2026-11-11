import sys
import unittest

from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):
    def setUp(self):
        self.task_pool = TaskPool()

    def test_add_task(self):
        task = Task("Test automated workflow")
        self.task_pool.add_task(task)

        self.assertEqual(len(self.task_pool.tasks), 1)
        self.assertEqual(self.task_pool.tasks[0].title, "Test automated workflow")
        self.assertEqual(self.task_pool.tasks[0].status, "ToDo")

    def test_get_open_tasks(self):
        self.task_pool.populate()
        open_tasks = self.task_pool.get_open_tasks()

        self.assertEqual(len(open_tasks), 3)
        self.assertTrue(all(task.status == "ToDo" for task in open_tasks))

    def test_get_done_tasks(self):
        self.task_pool.populate()
        done_tasks = self.task_pool.get_done_tasks()

        self.assertEqual(len(done_tasks), 3)
        self.assertTrue(all(task.status == "Done" for task in done_tasks))

    def test_mark_completed(self):
        task = Task("Complete CI/CD activity")
        task.mark_completed()

        self.assertTrue(task.completed)
        self.assertEqual(task.status, "Done")


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTaskPool)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    if result.wasSuccessful():
        print("\nAll task manager tests passed successfully.")
        sys.exit(0)

    print("\nOne or more task manager tests failed.")
    sys.exit(1)
