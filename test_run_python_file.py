# test_run_python_file.py
from functions.run_python_file import run_python_file

print("--- 1. run_python_file('calculator', 'main.py') ---")
print(run_python_file("calculator", "main.py"))
print()

print("--- 2. run_python_file('calculator', 'main.py', ['3 + 5']) ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print()

print("--- 3. run_python_file('calculator', 'tests.py') ---")
print(run_python_file("calculator", "tests.py"))
print()

print("--- 4. run_python_file('calculator', '../main.py') ---")
print(run_python_file("calculator", "../main.py"))
print()

print("--- 5. run_python_file('calculator', 'nonexistent.py') ---")
print(run_python_file("calculator", "nonexistent.py"))
print()

print("--- 6. run_python_file('calculator', 'lorem.txt') ---")
print(run_python_file("calculator", "lorem.txt"))