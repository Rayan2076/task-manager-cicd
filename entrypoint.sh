#!/bin/sh

set -e

echo "Starting Task Manager CI/CD activity."
echo "------------------------------------"

echo "Running the task manager application:"
python3 todo.py

echo ""
echo "Running automated unit tests:"
python3 todo-test.py

echo ""
echo "Task Manager CI/CD activity completed successfully."
