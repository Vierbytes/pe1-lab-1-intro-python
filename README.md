# Lab 1: Introduction to Python and Computer Programming

This repository contains the written answers and Python programs for Lab 1.

## Part 1: Written Exercise

### 1. What is computer programming, and why is it important?

Computer programming is writing instructions that tell a computer how to do a task. It is important because software helps people solve problems, organize information, and automate work in many parts of daily life.

### 2. What is Python, and why is it popular with beginners?

Python is a general-purpose programming language used for tasks such as scripting, web development, and data work. Its syntax is readable, so a beginner can focus on the steps in a program without learning a lot of punctuation first.

### 3. What tools do you need to write and run Python programs?

You need Python installed on your computer and a place to write code, such as a text editor or an IDE. You can download Python from the official Python website and follow the installer steps, then check it in a terminal with `python --version` or `python3 --version`. You can run a saved `.py` file with `python filename.py` or use the run feature in an IDE.

## Part 2: First Python Program

The `hello.py` file prints the two required lines:

```python
print("Hello, World!")
print("Welcome to Python programming.")
```

```text
Hello, World!
Welcome to Python programming.
```

## Part 3: Interactive Greeting

The `greeting.py` file asks for a name and handles an empty response.

```python
print("Hello, World!")
print("Welcome to Python programming.")

name = input("What is your name? ").strip()

if name:
    print(f"Hello, {name}! Glad to have you learning Python.")
else:
    print("Hello! Glad to have you learning Python.")
```

Example run:

```text
Hello, World!
Welcome to Python programming.
What is your name? Maya
Hello, Maya! Glad to have you learning Python.
```

I used `input()` to read the name and an f-string to include it in the greeting. Calling `.strip()` removes spaces at the beginning and end, and the `if` statement gives an answer when the input is empty.
