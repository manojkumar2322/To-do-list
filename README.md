# To-do-list

# To-Do List Application

This is a simple To-Do List application built using Python's Tkinter library and SQLite for persistent data storage. The application allows users to add tasks, delete tasks, mark tasks as done, and remove completed tasks.

## Features

- **Add Task:** Allows you to add a new task to the to-do list.
- **Delete Task:** Allows you to delete a selected task from the list.
- **Mark as Done:** Marks the selected task as done.
- **Remove Done Tasks:** Removes all tasks that are marked as done.
- **Persistent Storage:** Tasks are stored in an SQLite database, ensuring that they persist even after the application is closed.

## UI Color Scheme

- **Background Color:** Dark Green (`#2e8b57`)
- **Foreground Color:** Sandal (`#daa520`)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/todo-list-tkinter.git
    ```

2. Navigate to the project directory:

    ```bash
    cd todo-list-tkinter
    ```

3. Ensure you have Python installed. This application requires Python 3.x.

4. Run the application:

    ```bash
    python todo_list.py
    ```

## Usage

- **Add a Task:** Enter the task description in the input field and click the "Add Task" button.
- **Delete a Task:** Select a task from the list and click the "Delete Task" button.
- **Mark as Done:** Select a task from the list and click the "Mark as Done" button.
- **Remove Done Tasks:** Click the "Remove Done Tasks" button to delete all completed tasks.

## Code Overview

- **todo_list.py:** The main Python script that sets up the Tkinter GUI and connects to the SQLite database.

## Dependencies

- **Python 3.x**
- **Tkinter:** Typically included with Python.
- **SQLite3:** Typically included with Python.

## Future Enhancements

- Task sorting by date or priority.
- Ability to edit existing tasks.
- Notification or reminder feature for pending tasks.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact [your.email@example.com](mailto:your.email@example.com).
