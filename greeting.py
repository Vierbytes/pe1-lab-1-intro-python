"""Ask for a name and print a short greeting."""

print("Hello, World!")
print("Welcome to Python programming.")

name = input("What is your name? ").strip()

if name:
    print(f"Hello, {name}! Glad to have you learning Python.")
else:
    print("Hello! Glad to have you learning Python.")
