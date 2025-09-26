```markdown
# AI Coding Agent - Functionality Overview - As written by the agent itself

This AI Coding Agent provides a set of tools to interact with a file system within a secure, sandboxed environment. It allows users to:

*   **List Files and Directories:**  Explore the file structure within the working directory.
*   **Read File Content:** Inspect the contents of text-based files.  Files are truncated at 10,000 characters.
*   **Run Python Files:** Execute Python scripts with optional command-line arguments.
*   **Write Files:** Create new files or overwrite existing files with specified content.

## API Details

The agent exposes the following functions:

### `get_files_info(directory=None)`

Lists files and directories within a specified directory.

*   **Parameters:**
    *   `directory` (str, optional): The directory to list.  If `None`, lists the contents of the current working directory.
*   **Returns:**
    A dictionary containing file information (names and sizes).

### `get_file_content(file_path=None)`

Retrieves the content of a file.

*   **Parameters:**
    *   `file_path` (str, optional): The path to the file.
*   **Returns:**
    A dictionary containing the file content.  Note that files are truncated after the first 10,000 characters.

### `run_python_file(file_path=None, args=None)`

Executes a Python file.

*   **Parameters:**
    *   `file_path` (str, optional): The path to the Python file.
    *   `args` (str, optional): Command-line arguments to pass to the script.
*   **Returns:**
    A dictionary containing the output of the script execution.

### `write_file(file_path=None, content=None)`

Writes content to a file.  This will overwrite any existing file at the specified path.

*   **Parameters:**
    *   `file_path` (str, optional): The path to the file.
    *   `content` (str, optional): The content to write to the file.
*   **Returns:**
    A dictionary indicating the success of the write operation.

## Important Considerations

*   **Security:** All file operations are constrained to a designated working directory.  The agent cannot access files outside of this directory.
*   **File Size Limits:** The `get_file_content` function truncates files after 10,000 characters.
*   **Error Handling:**  The functions will return dictionaries indicating success or failure.  Check the contents of the returned dictionaries for error messages.
```