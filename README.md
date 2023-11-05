# framework_playwright_python

User manual: https://playwright.dev/python/

Test execution
-pytest: Execute all the test suite in headless mode.
-pytest --headed: Execute all the tests and show them in a browser.
-pytest --headed --browser XXX: Execute all the tests and show them in browser XXX.
-pytest tests/name_of_the_test.py: Execute only the tests in the file "name_of_the_test.py".
-pytest tests/testfile_1.py tests/test_file_2.py: Execute N number of py files.
-pytest -k string: Execute all tests that contains that string in their names.
-pytest --numprocesses N: Execute all tests in parallel in n machines (required pytest-xdist).