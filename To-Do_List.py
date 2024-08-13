import sys
import json
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QInputDialog, QMessageBox

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('To-Do List')
        self.setGeometry(100, 100, 400, 300)

        self.tasks = load_tasks()
        
        self.layout = QVBoxLayout()

        self.tasks_listbox = QListWidget()
        self.layout.addWidget(self.tasks_listbox)

        self.add_button = QPushButton('Add Task')
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.update_button = QPushButton('Update Task')
        self.update_button.clicked.connect(self.update_task)
        self.layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Delete Task')
        self.delete_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_button)

        self.exit_button = QPushButton('Save & Exit')
        self.exit_button.clicked.connect(self.on_exit)
        self.layout.addWidget(self.exit_button)

        self.setLayout(self.layout)
        self.load_tasks_to_listbox()

    def load_tasks_to_listbox(self):
        self.tasks_listbox.clear()
        for task in self.tasks:
            self.tasks_listbox.addItem(f"[{task['status']}] {task['title']} (Due: {task['deadline']})")

    def add_task(self):
        title, ok = QInputDialog.getText(self, 'Task Title', 'Enter task title:')
        if ok and title:
            description, ok = QInputDialog.getText(self, 'Task Description', 'Enter task description:')
            if ok:
                deadline, ok = QInputDialog.getText(self, 'Task Deadline', 'Enter task deadline (YYYY-MM-DD):')
                if ok:
                    task = {
                        'title': title,
                        'description': description,
                        'deadline': deadline,
                        'status': 'Pending'
                    }
                    self.tasks.append(task)
                    self.load_tasks_to_listbox()
                    QMessageBox.information(self, 'Task Added', 'Task added successfully!')

    def update_task(self):
        selected_task_idx = self.tasks_listbox.currentRow()
        if selected_task_idx != -1:
            task = self.tasks[selected_task_idx]
            if task['status'] == 'Pending':
                task['status'] = 'Completed'
                self.load_tasks_to_listbox()
                QMessageBox.information(self, 'Task Updated', 'Task marked as completed.')
            else:
                QMessageBox.warning(self, 'Warning', 'Task is already completed.')
        else:
            QMessageBox.warning(self, 'Warning', 'Please select a task to update.')

    def delete_task(self):
        selected_task_idx = self.tasks_listbox.currentRow()
        if selected_task_idx != -1:
            self.tasks.pop(selected_task_idx)
            self.load_tasks_to_listbox()
            QMessageBox.information(self, 'Task Deleted', 'Task deleted successfully!')
        else:
            QMessageBox.warning(self, 'Warning', 'Please select a task to delete.')

    def on_exit(self):
        save_tasks(self.tasks)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())