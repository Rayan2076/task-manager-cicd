FROM python:3.11-slim

WORKDIR /app

COPY todo.py /app/todo.py
COPY todo-test.py /app/todo-test.py
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
