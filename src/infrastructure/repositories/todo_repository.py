from src.domain.models.todo import Todo

class TodoRepository:
    def __init__(self):
        self._todos = []
        self._next_id = 1

    def get_all(self):
        return self._todos

    def get(self, todo_id: int):
        return next((t for t in self._todos if t.id == todo_id), None)

    def create(self, title: str, description: str):
        todo = Todo(id=self._next_id, title=title, description=description)
        self._todos.append(todo)
        self._next_id += 1
        return todo
