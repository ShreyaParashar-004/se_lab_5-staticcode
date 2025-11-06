# Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest issues to fix were style and minor cleanup tasks, such as removing unused imports and switching file operations to use context managers. These changes were straightforward and did not affect how the program worked. The hardest issues involved the mutable default argument and input type validation. These required a better understanding of Python’s function behavior and careful adjustments to avoid introducing new bugs.

## 2. Did the static analysis tools report any false positives? If so, describe one example.
There were no major false positives, but a few style warnings felt unnecessary for this specific assignment. Pylint flagged the old camelCase function names as problems even though the code still ran correctly. These warnings were useful for readability but did not indicate functional issues.

## 3. How would you integrate static analysis tools into your actual software development workflow?
I would use the tools locally while writing code and also include them in a continuous integration setup. Running Pylint, Flake8, and Bandit before committing code helps catch issues early. A GitHub Actions workflow would allow these tools to run automatically on each push or pull request, keeping the project consistent and preventing bad code from being merged.

## 4. What tangible improvements did you observe in the code quality, readability, or robustness after applying the fixes?
The code became cleaner and more reliable after applying the fixes. Removing the use of eval improved security. Adding type checks prevented unwanted crashes from invalid data. Rewriting functions to follow snake_case and adding docstrings made the program easier to read. Using context managers for file handling reduced the chance of resource issues. Overall, the program felt more structured and stable.
