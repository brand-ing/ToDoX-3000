# ToDoX-3000

ToDoX-3000 is a minimalistic, terminal-based to-do list application designed to help you manage tasks efficiently. With a clean interface and easy-to-use commands, it's a simple way to keep track of your to-dos directly from the terminal.

## Features

- Add, remove, and update tasks directly from the terminal.
- Organize tasks by priority and status (completed/incomplete).
- Minimal interface for distraction-free productivity.
- Easily view, list, and filter tasks.
- Supports a Pomodoro-like time tracking (optional future feature).
  
## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/brand-ing/ToDoX-3000.git
    ```

2. Navigate into the project directory:

    ```bash
    cd ToDoX-3000
    ```

3. Install dependencies (if any):

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python todox3000.py
    ```

## Usage

### Basic Commands

- **Add a task**:
    ```bash
    todox add "Your task description"
    ```

- **View tasks**:
    ```bash
    todox list
    ```

- **Mark task as complete**:
    ```bash
    todox complete <task_id>
    ```

- **Delete a task**:
    ```bash
    todox delete <task_id>
    ```

- **Filter tasks by priority**:
    ```bash
    todox list --priority high
    ```

### Options

- `--help`: Get a list of all commands and options.
  
## Development

To contribute to ToDoX-3000 or run tests:

1. Switch to the `development` branch:

    ```bash
    git checkout development
    ```

2. Run tests:

    ```bash
    # Example command, update based on your test system
    python -m unittest discover
    ```

3. Submit feature branches via pull requests.

## Project Structure

