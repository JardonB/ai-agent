from functions.get_file_content import get_file_content

test_cases = [
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py")
]

for test in test_cases:
    print(f'Result for "{test[1]}":\n{get_file_content(test[0], test[1])}')