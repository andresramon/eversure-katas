# User Story

As a user, I want to know if a year is a leap year, so that I can plan for an extra day on February 29th during those years.

## Acceptance Criteria

1. **All years divisible by 400 ARE leap years** - So, for example, 2000 was indeed a leap year.
2. **All years divisible by 100 but not by 400 are NOT leap years** - So, for example, 1700, 1800, and 1900 were NOT leap years, NOR will 2100 be a leap year.
3. **All years divisible by 4 but not by 100 ARE leap years** - E.g., 2008, 2012, 2016.
4. **All years not divisible by 4 are NOT leap years** - E.g. 2017, 2018, 2019.

--
To run the tests, run the following command from the root directory:

```bash
python.exe .\test_leap_year.py

```
