# test_get_file_content.py
from functions.get_file_content import get_file_content

# 1. Test lorem.txt truncation
result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")
print()

# 2. Test file lain dan kasus error
print("--- main.py ---")
print(get_file_content("calculator", "main.py"))
print()

print("--- pkg/calculator.py ---")
print(get_file_content("calculator", "pkg/calculator.py"))
print()

print("--- /bin/cat (Error case) ---")
print(get_file_content("calculator", "/bin/cat"))
print()

print("--- pkg/does_not_exist.py (Error case) ---")
print(get_file_content("calculator", "pkg/does_not_exist.py"))