## Code and Branch Coverage Testing

### Objective
The objective of this lab is to improve the test cases for the elevator dispatch application and measure statement and branch coverage using Python Coverage.py and pytest.

### Test Files
- `CodeCoverageTest_38_application.py` — Tests the application code to measure statement coverage.
- `BranchCoverageTest_38_application.py` — Tests different decision outcomes to measure branch coverage.

### Coverage Results
- **Statement coverage:** 100%
- **Branch coverage:** 100%
- **Statements missed:** 0
- **Branches:** 28
- **Partial branches:** 0

### Commands to Run

Statement coverage:

```bash
python -m coverage erase
python -m coverage run --source=elevator_dispatch -m pytest CodeCoverageTest_38_application.py -v
python -m coverage report -m
```

Branch coverage:

```bash
python -m coverage erase
python -m coverage run --branch --source=elevator_dispatch -m pytest BranchCoverageTest_38_application.py -v
python -m coverage report -m
```

### Conclusion
The test cases achieved 100% statement coverage and 100% branch coverage for the elevator dispatch application.
