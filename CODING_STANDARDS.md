# Sapiens 11 Python Coding Standards Document

## 1. Introduction

This document outlines the coding standards and conventions that our team adheres to for maintaining consistency, readability, and maintainability of our Python codebase. It serves as a guide to produce high-quality code and collaborate effectively. Adherence to these guidelines is crucial for code reviews, version control, and long-term maintenance.

## 2. Code Formatting (according to PEP-8)

- **Indentation**: Use 4 spaces per indentation level.
- **Line Length**: Max 79 characters for code and 72 for comments.
- **Imports**: Should be on separate lines and grouped in the standard order (standard library imports, related third-party imports, local application/library specific imports).
- **Whitespace in Expressions and Statements**: Follow PEP-8 guidelines for spacing around operators and after commas.
- **Comments**: Inline comments should be separated by at least two spaces from the statement.
- **Consistency**: The codebase should look as though it was written by one person, at all times.

## 3. Naming Conventions (according to PEP-8)

- **Modules**: Short, all-lowercase names, preferably without underscores.
- **Classes**: CapWords convention.
- **Functions**: Lowercase, with words separated by underscores as necessary to improve readability.
- **Variables**: Lowercase, with words separated by underscores.
- **Constants**: Upper case, with words separated by underscores. Non-API constants should start with `S11_` prefix.

## 4. Commenting (according to PEP-8)

- **File Docstrings**: At the beginning of every file, include a docstring describing the content and purpose of the file.
- **Class Docstrings**: Immediately following the class definition, provide a docstring with a description of the class.
- **Function Docstrings**: Every function should have a docstring that explains the function's purpose and behavior.
- **Section Comments**: Use comments to divide code into logical sections. Each section, like constants, should have a heading comment.

## 5. Language-Specific Idioms

Outline the preferred practices and idiomatic usage of Python, emphasizing clarity and Pythonic ways.

## 6. Error Handling

- Ensure all code sections that might throw exceptions handle them gracefully.
- Use specific exception handling rather than general catch-alls where possible.
- Include error codes in exceptions to guide users or developers in troubleshooting.
- High-level functions should implement broad exception handling to aggregate different errors into comprehensive messages.

## 7. Testing

- Unit tests must cover every function, mocking external dependencies, particularly the Large Language Model service requests.
- End-to-End tests should verify the system's behavior from the UI-UX/Client request level.
- **Example**: Demonstrate with Python code how to write a test case and mock a method.

## 8. Git Practices

Guidelines for using Git, including commit messages, branch naming, and pull requests.

## 9. Build and Deployment

Procedures and standards for building and deploying the codebase, covering automation and manual processes.

## 10. Security Practices

Best practices for secure coding, handling sensitive data, and conducting security reviews.

## 11. References

Links to external resources, Python coding standards, or tools that support these conventions.

## 12. Change Log Document

A separate document to be updated with each merged pull request, including:

- Merge commit references
- PR Title
- A description of what the PR does
- The developer that submitted the PR
- The developer that merged the PR
- The date of the merge

This document helps in tracking changes, reviewing the history of the codebase, and understanding the evolution of the project. It is crucial for maintaining a transparent and detailed project history.