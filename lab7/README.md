# Lab 7: Fuzz Testing for Input Validation Bugs

## 1. Experiment Title
Fuzz Testing for Input Validation Bugs using Hypothesis.

## 2. Objective
To perform fuzz testing on an Elevator Dispatch System using the Hypothesis library and Pytest to identify unexpected input handling errors and improve application reliability.

## 3. Tools and Technologies
- **Programming Language:** Python 3.12
- **Testing Framework:** Pytest
- **Fuzz Testing Library:** Hypothesis
- **Code Editor:** Visual Studio Code
- **Version Control:** Git
- **Repository Hosting:** GitHub

## 4. Project Description
The Elevator Dispatch System contains three main functions:

1. `parse_request()` – Validates elevator floor requests in the format `FROM->TO`.
2. `total_travel()` – Calculates the total distance travelled between consecutive floors.
3. `load_percent()` – Calculates the elevator load percentage using the format `X of Y`.

## 5. Fuzz Testing
Hypothesis was used to automatically generate unexpected inputs, including random strings and `None` values.

Initial fuzz testing identified input validation errors in all three functions. The errors occurred because the application performed string operations without checking the input type.

## 6. Bug Fixes
The following improvements were implemented:

- Added input type checking.
- Added input format validation.
- Added integer conversion error handling.
- Prevented negative load values.
- Prevented zero or negative capacity values.
- Added appropriate `ValueError` messages.

## 7. Project Files

```text
lab7/
│
├── README.md
├── elevator_dispatch.py
└── test_elevator_dispatch.py
```

## 8. How to Run the Application

Open Git Bash and navigate to the Lab 7 folder:

```bash
cd lab7
```

Run the application:

```bash
python elevator_dispatch.py
```

## 9. How to Run the Tests

Execute the following command:

```bash
python -m pytest test_elevator_dispatch.py -v
```

## 10. Final Test Results

- Total test cases: 7
- Passed: 7
- Failed: 0

All seven test cases passed successfully after implementing the input validation fixes.

## 11. Conclusion
Fuzz testing helped identify unexpected input handling errors in the Elevator Dispatch System. After implementing proper input validation and exception handling, all seven test cases passed successfully. This experiment demonstrated how fuzz testing improves software reliability and robustness.

---
**Submitted by:** Pavithra G C  
**Branch:** Computer Science and Engineering (CSE)  
**Institution:** PES University, Electronic City Campus
