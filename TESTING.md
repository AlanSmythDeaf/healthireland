# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

I had 238 issues, most of the issues were repetitive as I scroll down to all the issue, their were only six issues and they were
- E302 expected 2 blank lines, found 1
    - Solve the issue by adding another blank line
- W293 blank line contains whitespace
    - Solve the issue by removing the whitespace in the blank line
- E501 line too long (93 > 79 characters)
    - Solve the issue by removing the long line
- W291 trailing whitespace
    - Solve the issue by removing trailing white space
- E225 missing whitespace around operator
    - Solve the issue by adding whitespace 
- E305 expected 2 blank lines after class or function definition, found 1
    - Solve the issue by adding another blank line
- W292 no newline at end of file
    - Solve the issue by adding blank line after the end of the file


| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlanSmythDeaf/healthireland/main/run.py) | ![screenshot](documentation/pythonlinter/python-error1.png) | Issue with blank line, blank line containing white space, line too long |
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlanSmythDeaf/healthireland/main/run.py) | ![screenshot](documentation/pythonlinter/python-error2.png) | Issue with line too long, blank line contains whitespace, missing whitespace around operator
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlanSmythDeaf/healthireland/main/run.py) | ![screenshot](documentation/pythonlinter/python-error3.png) | Issue with line too long, blank line contains whitespace, two blank lines|
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AlanSmythDeaf/healthireland/main/run.py) | ![screenshot](documentation/pythonlinter/python-noerror.png) | All clear, no errors found |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/browser/chrome.png) | Works Fine  |
| Firefox | ![screenshot](documentation/browser/firefox.png) | Works Fine  |
| Edge | ![screenshot](documentation/browser/edge.png) | Works Fine  |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Main Menu | | | | | |
| | Expectation | Test | Result | Test concluded and passed | ![screenshot](documentation/features/feature01.png) |
| Body Mass Index | | | | | |
| | Expectation | Test | Result | Test concluded and passed | ![screenshot](documentation/features/feature03.png) |
| WAist to Hip Ratio | | | | | |
| | Expectation | Test | Result | Test concluded and passed | ![screenshot](documentation/features/feature05.png) |
| How it works | | | | | |
| | Expectation | Test | Result | Test concluded and passed | ![screenshot](documentation/features/feature07.png) |

## Bugs

## Unfixed Bugs
> [!NOTE]  
> There are no remaining bugs that I am aware of.
