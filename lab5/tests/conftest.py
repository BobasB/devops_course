def pytest_addoption(parser):
    parser.addoption("--url", action="store", help="An URL to HITS app (like http://hits:5000")